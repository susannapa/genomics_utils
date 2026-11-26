import argparse
import csv

DEFAULT_CHROMOSOMES = [f"chr{i}" for i in range(1, 23)] + ["chrX"]


def normalise_chrom(chrom):
    # accept both "1" (GRCh37 style) and "chr1"
    chrom = str(chrom)
    if chrom.startswith("chr"):
        return chrom
    return "chr" + chrom


def filter_rare_variants(variants, max_af=0.0005, max_ac=8, chromosomes=None):
    if chromosomes is None:
        chromosomes = DEFAULT_CHROMOSOMES

    filtered = []

    for variant in variants:
        af = variant.get("gnomad_af")
        ac = variant.get("gnomad_ac")
        chrom = variant.get("chrom")

        # skip variants without gnomAD annotation
        if af is None or ac is None:
            continue
        # rare variants only (default: gnomAD AF < 0.0005 and AC < 8)
        if af >= max_af:
            continue
        if ac >= max_ac:
            continue
        if normalise_chrom(chrom) not in chromosomes:
            continue

        filtered.append(variant)

    return filtered


def read_variants(path):
    # read a csv/tsv with columns chrom, pos, ref, alt, gnomad_af, gnomad_ac
    sep = "\t" if path.endswith((".tsv", ".txt")) else ","
    variants = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f, delimiter=sep)
        for row in reader:
            row["pos"] = int(row["pos"])
            row["gnomad_af"] = float(row["gnomad_af"]) if row["gnomad_af"] else None
            row["gnomad_ac"] = int(row["gnomad_ac"]) if row["gnomad_ac"] else None
            variants.append(row)
    return variants


def write_variants(variants, path):
    if not variants:
        open(path, "w").close()
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(variants[0].keys()))
        writer.writeheader()
        writer.writerows(variants)


def main():
    parser = argparse.ArgumentParser(description="Filter rare variants by gnomAD AF/AC and chromosome")
    parser.add_argument("input", help="csv or tsv with chrom, pos, ref, alt, gnomad_af, gnomad_ac")
    parser.add_argument("-o", "--output", help="output csv (default: print to screen)")
    parser.add_argument("--max-af", type=float, default=0.0005)
    parser.add_argument("--max-ac", type=int, default=8)
    parser.add_argument("--include-y", action="store_true", help="keep chrY variants too")
    args = parser.parse_args()

    chromosomes = DEFAULT_CHROMOSOMES + ["chrY"] if args.include_y else DEFAULT_CHROMOSOMES

    variants = read_variants(args.input)
    filtered = filter_rare_variants(variants, args.max_af, args.max_ac, chromosomes)
    print(f"{len(filtered)} of {len(variants)} variants kept")

    if args.output:
        write_variants(filtered, args.output)
    else:
        for v in filtered:
            print(v)


if __name__ == "__main__":
    main()
