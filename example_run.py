from rare_variant_filter import filter_rare_variants

#load variants
variants = []
with open("input_variants.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        variant = {
            "chrom": row["chrom"],
            "pos": int(row["pos"]),
            "ref": row["ref"],
            "alt": row["alt"],
            "gnomad_af": float(row["gnomad_af"]) if row["gnomad_af"] else None,
            "gnomad_ac": int(row["gnomad_ac"]) if row["gnomad_ac"] else None
        }
        variants.append(variant)

#filter
filtered = filter_rare_variants(variants)

#print results
print("Filtered variants:")
for v in filtered:
    print(v)
