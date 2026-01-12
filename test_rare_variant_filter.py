from rare_variant_filter import filter_rare_variants

def test_keep_autosome():
    variants = [
        {
            "chrom": "chr1",
            "pos": 123456,
            "ref": "A",
            "alt": "G",
            "gnomad_af": 0.0001,
            "gnomad_ac": 2,
        }
    ]
    result = filter_rare_variants(variants)
    assert len(result) == 1
    assert result[0]["chrom"] == "chr1"


def test_af():
    variants = [
        {
            "chrom": "chr1",
            "pos": 123456,
            "ref": "A",
            "alt": "G",
            "gnomad_af": 0.01,
            "gnomad_ac": 2,
        }
    ]
    result = filter_rare_variants(variants)
    assert result == []


def test_ac():
    variants = [
        {
            "chrom": "chr1",
            "pos": 123456,
            "ref": "A",
            "alt": "G",
            "gnomad_af": 0.0001,
            "gnomad_ac": 22,
        }
    ]
    result = filter_rare_variants(variants)
    assert result == []

def test_skip_missing_gnomad():
    variants = [
        {
            "chrom": "chr1",
            "pos": 123456,
            "ref": "A",
            "alt": "G",
            "gnomad_af": None,
            "gnomad_ac": 2,
        }
    ]
    result = filter_rare_variants(variants)
    assert result == []

def test_filter_chr():
    variants = [
        {
            "chrom": "chrY",
            "pos": 123456,
            "ref": "A",
            "alt": "G",
            "gnomad_af": 0.0001,
            "gnomad_ac": 2,
        }
    ]
    result = filter_rare_variants(variants)
    assert result == []
