#define an exception class for non-existing base pairs
class UnknownBaseException(Exception):
    pass

#implement our list of tests
test = [
    #input      #expected_output
    ['gtcagtc', {'G':2, 'T':2, 'C':2, 'A':1}], #function should always return nucleotide content using uppercase letters for the dictionary keys.
    ['gtagt',   {'G':2, 'T':2, 'A':1}],        #if a nucleotide is missing, ignore it in the output dictionary
    ['GTCNGAT', UnknownBaseException]          #if a character other than ACTG exists in the string, raise an exception
]

def nucleotideContent(dnaString):    
    '''This function must return the contribution of nucleotides 
    ATCG (as uppercase) from a given DNA string inside a dictionary, 
    where each key refers to a nucleotide. It returns an error if
    characters other than ATCG are found in the input dnaString
    '''  
    
    dnaString=dnaString.upper() #convert string into uppercase letters
    
    
    dnaDict             = {} #create empty dictionary to store output   
    uniques             = set(dnaString) #get unique values for the string
    intersected_uniques = uniques.intersection(set('ACTG'))
    
    if len(uniques) != len(intersected_uniques): #if they differ, this means that dnaString has characters different than 'ACTG' - this defines, for example, that RNA strings are not accepted either
        raise UnknownBaseException()  
         
    for nucleotide in uniques: #loops through ATCG and add their respective counts to the output dictionary 
        dnaDict[nucleotide]=dnaString.count(nucleotide)    
    
    return dnaDict


# Run and report    
passes = 0 #starts number of    
for (i, (seq, expected)) in enumerate(test): #enumerates each line of our test list and seq and expected take the respective values inside each sublist (i.e. element) of test
    if expected == UnknownBaseException: #if the expected result is an UnknownBaseException exception class 
        try:
            nucleotideContent(seq) #checks if there's an error with the input test string seq
        except expected: #if the error occurs, pass the test, as that's what we expect to happen anyway
            passes += 1
    else: #else just continue with the standard routine
        if nucleotideContent(seq) == expected:    
            passes += 1    
        else:    
            print('test %d failed' % i) #if a test line fails, print it so it makes debugging faster   
    
print('%d/%d tests passed' % (passes, len(test)))