# Rare variant filtering script

![tests](https://github.com/susannapa/genomics_utils/actions/workflows/tests.yml/badge.svg)

Python script to filter rare genetic variants from WGS/WES based on chromosome, gnomAD AF and AC.

### Features
- Filter variants with (defaults, can be changed):
  - `gnomAD AF < 0.0005`
  - `gnomAD AC < 8`
  - Chromosomes: chr1–chr22, chrX (chrY optional)
- Works with `chr1` and `1` style chromosome names
- Reads csv or tsv files, writes csv
- Tests with `pytest` (run automatically on GitHub)
- Docker image

### Installation
```bash
git clone https://github.com/susannapa/genomics_utils.git
cd genomics_utils
```
No extra packages needed (only Python 3). `pytest` for the tests.

### Usage
From the command line:
```bash
python rare_variant_filter.py input_variants.csv -o rare_variants.csv
python rare_variant_filter.py input_variants.csv --max-af 0.0001 --max-ac 5
python rare_variant_filter.py input_variants.csv --include-y
```

The input needs these columns: `chrom, pos, ref, alt, gnomad_af, gnomad_ac` (see `input_variants.csv`).
Variants without gnomAD AF or AC are removed.

From Python:
```python
from rare_variant_filter import filter_rare_variants

variants = [
    {"chrom": "chr1", "pos": 123456, "ref": "A", "alt": "G", "gnomad_af": 0.0001, "gnomad_ac": 2},
    {"chrom": "chr2", "pos": 234567, "ref": "T", "alt": "C", "gnomad_af": 0.001, "gnomad_ac": 1},
]

filtered = filter_rare_variants(variants)
filtered = filter_rare_variants(variants, max_af=0.0001, max_ac=5)
```

### Example run
```bash
python example_run.py
```

### Docker
```bash
docker build -t rare-variant-filter .
docker run rare-variant-filter                                          # example file
docker run -v $(pwd):/data rare-variant-filter /data/my_variants.csv    # your own file
```

### Testing
```bash
pytest test_rare_variant_filter.py
```
