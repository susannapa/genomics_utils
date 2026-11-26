from rare_variant_filter import filter_rare_variants, read_variants, write_variants


def make_variant(chrom="chr1", af=0.0001, ac=2):
    return {"chrom": chrom, "pos": 123456, "ref": "A", "alt": "G", "gnomad_af": af, "gnomad_ac": ac}


def test_keep_autosome():
    result = filter_rare_variants([make_variant()])
    assert len(result) == 1
    assert result[0]["chrom"] == "chr1"


def test_af():
    assert filter_rare_variants([make_variant(af=0.01)]) == []


def test_ac():
    assert filter_rare_variants([make_variant(ac=22)]) == []


def test_af_at_cutoff_is_removed():
    # cutoff is strict: AF must be below 0.0005
    assert filter_rare_variants([make_variant(af=0.0005)]) == []


def test_skip_missing_gnomad():
    assert filter_rare_variants([make_variant(af=None)]) == []
    assert filter_rare_variants([make_variant(ac=None)]) == []


def test_filter_chr():
    assert filter_rare_variants([make_variant(chrom="chrY")]) == []


def test_keep_chrx():
    assert len(filter_rare_variants([make_variant(chrom="chrX")])) == 1


def test_chrom_without_chr_prefix():
    # GRCh37 style names should work too
    assert len(filter_rare_variants([make_variant(chrom="1")])) == 1
    assert filter_rare_variants([make_variant(chrom="Y")]) == []


def test_custom_thresholds():
    v = make_variant(af=0.0002, ac=5)
    assert filter_rare_variants([v], max_af=0.0001) == []
    assert filter_rare_variants([v], max_ac=3) == []
    assert len(filter_rare_variants([v], max_af=0.001, max_ac=10)) == 1


def test_include_chry():
    chroms = [f"chr{i}" for i in range(1, 23)] + ["chrX", "chrY"]
    assert len(filter_rare_variants([make_variant(chrom="chrY")], chromosomes=chroms)) == 1


def test_read_and_write(tmp_path):
    infile = tmp_path / "in.csv"
    infile.write_text("chrom,pos,ref,alt,gnomad_af,gnomad_ac\n"
                      "chr1,100,A,G,0.0001,2\n"
                      "chr2,200,T,C,,\n")
    variants = read_variants(str(infile))
    assert variants[0]["gnomad_af"] == 0.0001
    assert variants[1]["gnomad_af"] is None

    outfile = tmp_path / "out.csv"
    write_variants(filter_rare_variants(variants), str(outfile))
    lines = outfile.read_text().splitlines()
    assert len(lines) == 2  # header + 1 variant


def test_read_tsv(tmp_path):
    infile = tmp_path / "in.tsv"
    infile.write_text("chrom\tpos\tref\talt\tgnomad_af\tgnomad_ac\nchr1\t100\tA\tG\t0.0001\t2\n")
    assert read_variants(str(infile))[0]["pos"] == 100
