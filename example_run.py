from rare_variant_filter import filter_rare_variants, read_variants

#load variants
variants = read_variants("input_variants.csv")

#filter
filtered = filter_rare_variants(variants)

#print results
print("Filtered variants:")
for v in filtered:
    print(v)
