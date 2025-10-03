#!/usr/bin/env python3
import argparse
import sys

import pandas as pd
import pyranges as pr

REF_SIZES = {
    "37": 3_137_144_693,
    "38": 3_095_677_412,
}


def load_gene_list(gene_file):
    genes = set()
    with open(gene_file) as f:
        for line in f:
            gene = line.strip()
            if gene:
                genes.add(gene.upper())
    return genes


def load_chrom_sizes(chrom_file):
    sizes = {}
    with open(chrom_file) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                chrom, size = parts[0], int(parts[1])
                sizes[chrom] = size
    return sizes


def normalize_chr_col(df, col, keep_chr):
    if not keep_chr:
        # remove leading "chr" if present
        df[col] = df[col].astype(str).str.replace(r"^chr", "", regex=True)
    return df


def write_bed(out, chrom, start, end, name, score, strand, gene_id, info="."):
    """Write one standardized BED line with 8 columns."""
    out.write(
        f"{chrom}\t{start}\t{end}\t{name}\t{score}\t{strand}\t{gene_id}\t{info}\n"
    )


def merge_bed(in_bed, out_bed, merge_stranded=True):
    """
    Optionally merge overlapping BED intervals using pybedtools.

    Parameters
    ----------
    in_bed : str
        Path to the input BED file (8-column from this script).
    out_bed : str
        Path to save the merged BED file.
    merge_stranded : bool, default=True
        If True, merges only features on the same strand (-s flag in bedtools).
    """
    import pybedtools

    bed = pybedtools.BedTool(in_bed)

    # Sort before merging
    bed = bed.sort()

    merged = bed.merge(
        s=merge_stranded,
        c=[4, 5, 6, 7, 8],
        o=["collapse", "distinct", "distinct", "distinct", "collapse"],
        delim="|",
    )

    merged.saveas(out_bed)
    return out_bed


def main():
    parser = argparse.ArgumentParser(
        description="Generate BED file for adaptive sampling; "
        "annotate segdups (intersection done on dsbuffer only)"
    )
    parser.add_argument(
        "--annotation",
        required=True,
        help="Gene annotation file (tab-delimited). Expected columns: "
        "chrom, start, end, gene_id, gene_symbol",
    )
    parser.add_argument(
        "--genes", required=True, help="File with target gene symbols (one per line)"
    )
    parser.add_argument(
        "--dsbuffer",
        type=int,
        default=20000,
        help="Number of bases to extend upstream/downstream (gene body padding)",
    )
    parser.add_argument(
        "--ssbuffer",
        type=int,
        default=30000,
        help="Number of bases to extend at transcript side "
        "(applied on top of dsbuffer)",
    )
    parser.add_argument(
        "--chr_option",
        choices=["yes", "no"],
        default="yes",
        help="Retain 'chr' prefix in chromosome names (default: yes). "
        "Use 'no' to strip leading 'chr'.",
    )
    parser.add_argument(
        "--mode",
        choices=["strand-specific", "merged"],
        default="strand-specific",
        help="Output mode: 'strand-specific' (two BED lines per gene) "
        "or 'merged' (one interval, strand '.')",
    )
    parser.add_argument(
        "--ref",
        choices=["37", "38"],
        default="38",
        help="Reference: choose from 37 or 38 (default: 38) "
        "used for percent calculations",
    )
    parser.add_argument(
        "--chrom_sizes", required=True, help="File with chromosome sizes (chrom\\tsize)"
    )
    parser.add_argument(
        "--segdups",
        required=True,
        help="UCSC genomicSuperDups file (headered). "
        "Will read chrom, chromStart, chromEnd, "
        "otherChrom, otherStart, otherEnd, fracMatchIndel.",
    )
    parser.add_argument(
        "--segdup_cutoff",
        type=float,
        default=0.95,
        help="Minimum fracMatchIndel to keep segdup overlaps (default 0.95)",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output BED file (tab-delimited). "
        "Columns: chrom start end name score strand gene_id metadata",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Optionally merge overlapping intervals "
        "in the final BED (strand-specific if mode=strand-specific).",
    )
    args = parser.parse_args()

    keep_chr = args.chr_option == "yes"

    # Load reference data
    genome_size = REF_SIZES.get(args.ref)
    if genome_size is None:
        parser.error(f"Unknown reference {args.ref}")
    target_genes = load_gene_list(args.genes)
    chrom_sizes = load_chrom_sizes(args.chrom_sizes)

    totalROI = 0
    totalBP = 0

    # collect: (1) ds-only intervals for segdup intersection;
    #          (2) output padded intervals (strand-specific or merged) to write later
    ds_records = (
        []
    )  # one ds-padded interval per gene: Chromosome, Start, End, Gene, GeneID
    out_records = (
        []
    )  # final output rows: chrom, start, end, name, score, strand, gene_id, metadata

    with open(args.annotation) as annot:
        for line in annot:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 5:
                sys.stderr.write(
                    f"Warning: annotation line doesn't have >=5 cols: {line}\n"
                )
                continue

            chrom = parts[0]
            start = int(parts[1])
            end = int(parts[2])
            gene_id = parts[3]
            gene_symbol = parts[4].upper()

            if gene_symbol not in target_genes:
                continue

            if not keep_chr and chrom.startswith("chr"):
                chrom = chrom[3:]

            if chrom not in chrom_sizes:
                sys.stderr.write(
                    f"Warning: {chrom} not found in "
                    "chromosome sizes file. Skipping {gene_symbol}.\n"
                )
                continue
            chr_len = chrom_sizes[chrom]

            gene_length = max(0, end - start)
            totalROI += gene_length

            # gene-body ds padding (this is the interval used for segdup intersection)
            start_ds = max(0, start - args.dsbuffer)
            end_ds = min(chr_len, end + args.dsbuffer)
            # store ds interval (single per gene)
            ds_records.append((chrom, start_ds, end_ds, gene_symbol, gene_id))

            # Now create the output padded intervals (ssbuffer applied on top of ds)
            if args.mode == "strand-specific":
                # + strand: ss padding applied to LEFT of ds-padded start
                plus_start = max(0, start_ds - args.ssbuffer)
                plus_end = end_ds
                plus_len = max(0, plus_end - plus_start)
                totalBP += plus_len
                out_records.append(
                    (chrom, plus_start, plus_end, gene_symbol, 0, "+", gene_id, ".")
                )

                # - strand: ss padding applied to RIGHT of ds-padded end
                minus_start = start_ds
                minus_end = min(chr_len, end_ds + args.ssbuffer)
                minus_len = max(0, minus_end - minus_start)
                totalBP += minus_len
                out_records.append(
                    (chrom, minus_start, minus_end, gene_symbol, 0, "-", gene_id, ".")
                )

            else:  # merged
                merged_start = start_ds
                merged_end = end_ds
                merged_len = max(0, merged_end - merged_start)
                totalBP += merged_len
                out_records.append(
                    (chrom, merged_start, merged_end, gene_symbol, 0, ".", gene_id, ".")
                )

    # Build dataframe for ds intervals
    if len(ds_records) == 0:
        sys.stderr.write("No target genes found (empty ds_records). Exiting.\n")
        return

    df_ds = pd.DataFrame(
        ds_records, columns=["Chromosome", "Start", "End", "Gene", "GeneID"]
    )

    # --- read segdups file (headered UCSC genomicSuperDups) ---
    usecols = [
        "chrom",
        "chromStart",
        "chromEnd",
        "otherChrom",
        "otherStart",
        "otherEnd",
        "fracMatchIndel",
    ]
    try:
        df_segdup = pd.read_csv(
            args.segdups,
            sep="\t",
            usecols=usecols,
            dtype={"chrom": str, "otherChrom": str},
        )
    except Exception as e:
        sys.stderr.write(f"Error reading segdups file: {e}\n")
        sys.stderr.write(
            "Expected a headered UCSC genomicSuperDups file with columns including: "
            + ", ".join(usecols)
            + "\n"
        )
        raise

    # normalize chr prefix to match annotation handling
    if not keep_chr:
        df_segdup["chrom"] = (
            df_segdup["chrom"].astype(str).str.replace(r"^chr", "", regex=True)
        )
        df_segdup["otherChrom"] = (
            df_segdup["otherChrom"].astype(str).str.replace(r"^chr", "", regex=True)
        )

    # rename to PyRanges conventions
    df_segdup = df_segdup.rename(
        columns={"chrom": "Chromosome", "chromStart": "Start", "chromEnd": "End"}
    )

    # convert to PyRanges and join (intersection done on ds-padded intervals only)
    pr_ds = pr.PyRanges(df_ds)  # has Chromosome, Start, End, Gene, GeneID
    pr_seg = pr.PyRanges(
        df_segdup
    )  # has Chromosome, Start, End, otherChrom, otherStart, otherEnd, fracMatchIndel

    pr_joined = pr_ds.join(pr_seg)
    df_joined = pr_joined.df

    # Filter by fracMatchIndel cutoff and drop NA
    if "fracMatchIndel" in df_joined.columns:
        df_joined = df_joined[
            df_joined["fracMatchIndel"].notna()
            & (df_joined["fracMatchIndel"] >= args.segdup_cutoff)
        ].copy()
    else:
        df_joined = df_joined.iloc[0:0].copy()  # empty

    segdup_added = 0
    if not df_joined.empty:
        df_joined["otherStart"] = df_joined["otherStart"].astype(int)
        df_joined["otherEnd"] = df_joined["otherEnd"].astype(int)

        for _, r in df_joined.iterrows():
            frac = float(r["fracMatchIndel"])
            frac_str = f"{frac:.3f}"
            base_name = f"segdup_of_{r['Gene']}_fracMatch_{frac_str}"
            metadata = (
                f"src:{r['Chromosome']}:{int(r['Start'])}-{int(r['End'])};"
                f"other:{r['otherChrom']}:{int(r['otherStart'])}-{int(r['otherEnd'])};"
                f"fracMatchIndel:{frac_str}"
            )

            o_chrom = r["otherChrom"]
            o_start = r["otherStart"]
            o_end = r["otherEnd"]

            if o_chrom not in chrom_sizes:
                continue
            chr_len = chrom_sizes[o_chrom]

            # Apply strand-specific padding if requested
            if args.mode == "strand-specific":
                # + strand: pad left side
                plus_start = max(0, o_start - args.ssbuffer)
                plus_end = o_end
                out_records.append(
                    (
                        o_chrom,
                        plus_start,
                        plus_end,
                        base_name,
                        0,
                        "+",
                        r["GeneID"],
                        metadata,
                    )
                )

                # - strand: pad right side
                minus_start = o_start
                minus_end = min(chr_len, o_end + args.ssbuffer)
                out_records.append(
                    (
                        o_chrom,
                        minus_start,
                        minus_end,
                        base_name,
                        0,
                        "-",
                        r["GeneID"],
                        metadata,
                    )
                )
            else:
                # merged: no strand, just interval
                out_records.append(
                    (o_chrom, o_start, o_end, base_name, 0, ".", r["GeneID"], metadata)
                )

            segdup_added += 1

    # Write combined output: original padded gene intervals
    # followed by segdup partner intervals (if any)
    df_out = pd.DataFrame(
        out_records,
        columns=[
            "chrom",
            "start",
            "end",
            "name",
            "score",
            "strand",
            "gene_id",
            "metadata",
        ],
    )
    # Ensure integer coords
    df_out["start"] = df_out["start"].astype(int)
    df_out["end"] = df_out["end"].astype(int)

    df_out.to_csv(args.output, sep="\t", header=False, index=False)

    # Optional merge
    if args.merge:
        sys.stderr.write("Merging overlapping intervals...\n")
        merge_bed(
            args.output, args.output, merge_stranded=(args.mode == "strand-specific")
        )

    # Stats
    roi_percent = (totalROI / genome_size) * 100.0
    denom = genome_size * 2 if args.mode == "strand-specific" else genome_size
    bp_percent = (totalBP / denom) * 100.0

    sys.stderr.write(
        f"{'Total ROI (gene length):':35s} {totalROI:>12,d} bp "
        f"({roi_percent:8.4f}% of GRCh{args.ref})\n"
    )

    ref_label = (
        f"GRCh{args.ref} (stranded)"
        if args.mode == "strand-specific"
        else f"GRCh{args.ref}"
    )

    sys.stderr.write(
        f"{'Total BP (target length with buffer):':35s} {totalBP:>12,d} bp "
        f"({bp_percent:8.4f}% of {ref_label})\n"
    )

    sys.stderr.write(f"{'Segdup partner intervals added:':35s} {segdup_added:>12,d}\n")


if __name__ == "__main__":
    main()
