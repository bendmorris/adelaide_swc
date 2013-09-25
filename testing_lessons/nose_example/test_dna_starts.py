def dna_starts_with(st1, st2):
    return st1[0:len(st2)]==st2

def test_starts_with_itself():
  dna = 'actgt'
  assert dna_starts_with(dna, dna)

def test_starts_with_single_base_pair():
  assert dna_starts_with('actg', 'a')

def test_does_not_start_with_single_base_pair():
  assert not dna_starts_with('ttct', 'a')

