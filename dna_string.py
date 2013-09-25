# gc_content
# base_count('G')
# reverse_complement
#   G<->C
#   T<->A


class NucleotideString:
    base_complement = {'G': 'C', 'C':'G',
                       'A': 'T', 'T': 'A'}
    
    def __init__(self, sequence):
        self.sequence = sequence
    
    def base_count(self, base):
        '''Count the number of times the specified
        base occurs in the sequence.'''
        return self.sequence.count(base)

    def gc_content(self):
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)

    def reverse_complement(self):
        complement = ''        
        for base in self.sequence:
            complement = self.base_complement[base] + complement
        
        return complement


# DNAString is a specific instance of
# NucleotideString that uses the bases
# GATC
class DNAString(NucleotideString):
    pass


# RNAString uses the bases GAUC
class RNAString(NucleotideString):
    base_complement = {'G': 'C', 'C':'G',
                       'A': 'U', 'U': 'A'}
