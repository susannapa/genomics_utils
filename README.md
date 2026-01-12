# Rare variant filtering script

Python script to filter rare genetic variants from WGS/WES based on chr, gnomAD AF and AC.

### Features
- Filter variants with:
  - `gnomAD AF < 0.0005`
  - `gnomAD AC < 8`
  - Chromosomes: chr1–chr22, chrX
- Includes automated testing with `pytest`.

### Installation
Clone this repo:

```bash
git clone https://github.com/susannapa/rare_variant_filter.git
cd rare_variant_filter

```

### Usage
from rare_variant_filter import filter_rare_variants

variants = [
    {"chrom": "chr1", "pos": 123456, "ref": "A", "alt": "G", "gnomad_af": 0.0001, "gnomad_ac": 2},
    {"chrom": "chr2", "pos": 234567, "ref": "T", "alt": "C", "gnomad_af": 0.001, "gnomad_ac": 1}
]

filtered = filter_rare_variants(variants)
print(filtered)

### Example run
You can also run the script on a CSV input with:

python example_run.py

### Testing
pytest test_rare_variant_filter.py


