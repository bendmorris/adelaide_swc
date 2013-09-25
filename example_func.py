#Exercise 1:

#given a string 'dna', remove all 'N', return the GC-content

def count_gc_content(dna):
    dna = dna.replace('N','')
    gc = dna.count('C') + dna.count('G')
    return gc/float(len(dna))

dna  = 'ATGCNNNNNNNN' # should be 0.5
dna2 = 'NGGGGGGGGGGGC' # should be 1
dna3 = 'GTGTGTGTGTGTTT' # should be 0.75

print count_gc_content(dna)
print count_gc_content(dna2)
print count_gc_content(dna3)
