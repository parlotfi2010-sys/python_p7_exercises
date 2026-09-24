#Exercise 1 :

#1.1.find_max_price :

products = {'laptop' : 1200,
            'phone' : 800,
            'tablet' : 500,
            'headphone' : 150,
            'mouse' : 50}

def find_max_price(products):
    '''
    This function checks the prices in this dictionary(products)
    and returns the maximum price.

    Parameters
    ----------
    products : TYPE, dict
        Dictionary of products.

    Returns
    -------
    maximum_price : TYPE, int
        Maximum price in the products dictionary.
    '''
    
    maximum_price = 0
    
    for price in products.values() :
        if price > maximum_price :
            maximum_price = price  
    return maximum_price

result = find_max_price(products)
print ('Maximum price : ' , result)

#man be do ravesh raftam, raveshe 2 :
    
def max_price(products) :
    '''
    This function checks the prices in this dictionary(products)
    and returns the maximum price.

    Parameters
    ----------
    products : TYPE, dict
        Dictionary of products.

    Returns
    -------
    maximum_price : TYPE, int
        Maximum price in the products dictionary.
    '''
    
    prices_list = list(products.values())
    maximum_price = prices_list[0]
    
    for price in prices_list :
        if price > maximum_price :
            maximum_price = price
    return maximum_price

result = max_price(products)
print ('Maximum price : ' , result)

#1.2.most_expensive_product :
    
def most_expensive_product(products) :
    '''
    This function checks the prices and find the name of the most expensive product
    in this dictionary(products) and returns the name of the most expensive product.

    Parameters
    ----------
    products : TYPE, dict
        Dictionary of products.

    Returns
    -------
    product_name : TYPE, str
        The name of the most expensive product.
    '''
    maximum_price = 0
    product_name = None
    
    for product,price in products.items() :
        if price > maximum_price :
            maximum_price = price
            product_name = product
    return product_name

result = most_expensive_product(products)
print ('The most expensive product : ' , result)

#1.3.find_min_price :
    
def find_min_price(products) :
    '''
    This function checks the prices in this dictionary(products)
    and returns the minimum price.

    Parameters
    ----------
    products : TYPE, dict
        Dictionary of products.

    Returns
    -------
    minimum_price : TYPE, int
        Minimum price in the products dictionary.
    '''

    prices_list = list(products.values())
    minimum_price = prices_list[0]
    
    for price in prices_list :
        if price < minimum_price :
            minimum_price = price
    return minimum_price

result = find_min_price(products)
print ('Minimum price : ' , result)

#1.4.cheapest_product :
    
def cheapest_product(products) :
    '''
    This function checks the prices and find the name of the cheapest product
    in this dictionary(products) and returns the name of the cheapest product.
    
    Parameters
    ----------
    products : TYPE, dict
        Dictionary of products.

    Returns
    -------
    product_name : TYPE, str
        The name of the cheapest product.
    '''

    minimum_price = list(products.values())[0]
    product_name = None
    
    for product,price in products.items() :
        if price < minimum_price :
            minimum_price = price
            product_name = product            
    return product_name

result = cheapest_product(products)
print ('The cheapest product : ' , result)

#1.5.total_price :

def total_price(products) :
    '''
    This function returns the total of prices in the products dictionary.

    Parameters
    ----------
    products : TYPE, dict
        Dictionary of products.
        
    Returns
    -------
    total : TYPE, int
        Total price of all products.
    '''

    total = 0
    
    for price in products.values() :
        total = total + price
    return total

result = total_price(products)
print('Total price : ' , result)

#1.6.average_price :
    
def average_price(products) :
    '''
    This function returns the average of prices in the products dictionary.

    Parameters
    ----------
    products : TYPE, int
        Dictionary of products.

    Returns
    -------
    average : TYPE, int
    Avwrage price of all products.
    
    '''

    total = 0
    count = 0
    
    for price in products.values() :
        total = total + price
        count = count + 1
        
    average = total / count
    return average

result = average_price(products)
print('Average price : ' , result)
        