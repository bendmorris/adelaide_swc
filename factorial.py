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
    import doctest
    doctest.testmod()


