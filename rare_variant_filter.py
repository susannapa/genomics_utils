
def filter_rare_variants(variants):
    allowed_chromosomes = [f"chr{i}" for i in range(1,23)]+["chrX"]

    filtered = []

    for variant in variants:
        af = variant.get("gnomad_af")
        ac = variant.get("gnomad_ac")
        chrom = variant.get("chrom")

        if af is None or ac is None:
            continue
        # get rare variants only (gnomAD AF < 0.0005 and gnomAD AC <8)
        if af >= 0.0005:
            continue
        if ac >= 8:
            continue
        if chrom not in allowed_chromosomes:
            continue

        filtered.append(variant)

    return filtered
