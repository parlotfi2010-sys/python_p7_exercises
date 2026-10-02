#Optional 1_l8 :
    

def even_numbers(n) :
    '''
    This function is created to generate even numbers from 2 up to n.

    Parameters
    ----------
    n : TYPE, int
        The number that is received.

    Yields
    ------
    TYPE, int
        Generate integer number and even number one by one.
    '''
    
    for number in range(2 , n , 2) :
        yield number

number = even_numbers(8)
print(next(number))
print(next(number))
print(next(number))
