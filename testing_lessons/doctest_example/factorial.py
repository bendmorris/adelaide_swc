#for more complete usage of doctest, go to:
#http://docs.python.org/2/library/doctest.html

def factorial(n):
    '''Return the factorial of n, an integer >= 0
    
    >>> factorial(4)
    24
    '''
    import math
    if not n >= 0:
        raise ValueError('n must be >= 0')
    
    if math.floor(n) != n:
        raise ValueError('n mus be integer')
    
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor +=  1
    
    return result

if __name__ == '__main__':
    # when importing this file, the doctests aren't run
    # but when you run the file with python, the doctests are run
    import doctest
    doctest.testmod()


