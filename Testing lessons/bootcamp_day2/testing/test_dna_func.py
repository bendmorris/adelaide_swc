def dna_starts_with(st1,st2):
    return st1[0:len(st2)]==st2

def test_dna_itself():
    dna='atcgt'
    assert dna_starts_with(dna,dna)

def test_dna_different():
    assert not dna_starts_with('atcgtg','t')

test_dna_itself()
test_dna_different()
