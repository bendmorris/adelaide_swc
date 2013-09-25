# exercise 2:
'''
Given a string 'filename', write a function which opens that file, iterates over all sequences, and writes a bit of stats about each sequence:

- print the name of each sequence
- Count of Ns
- GC-content

Print amount of sequences in that file.

Tips: 
-  if line.startswith('>') - give the name
'''
def give_dna_stats(filename):
  fh = open(filename, 'r')
  line = fh.readline()
  sequence_counter = 0
  while line != '':
    line = line.rstrip()
    if line.startswith('>'):
      print 'The name of the sequence is ', line
      
    else:
      line = line.upper()
      gc_count = float(line.count('G') + line.count('C'))/len(line.replace('N', ''))
      n_count = line.count('N')
      print 'GC-content is ' +  str(gc_count)
      print 'There are ' + str(n_count)  + ' Ns.'
      sequence_counter += 1
    line = fh.readline()
  print 'There are ' + str(sequence_counter) + ' sequences in the file.'
  
give_dna_stats('example.fasta')
