#Optional 2_l8 :

products = {"laptop": 3,
            "phone": 0,
            "tablet": 5,
            "mouse": 0,
            "keyboard": 2}

def available_products(products) :
    '''
    This function is generate one by one the names of products
    with stock greater than zero.

    Parameters
    ----------
    products : TYPE, dict
        A product dictionary.
        
    Yields
    ----------
    TYPE, str
        Name of product.

    '''
    
    for key, value in products.items() :
        if value > 0 :
            yield key

Generator = available_products(products)

print(next(Generator))
print(next(Generator))
print(next(Generator))
    