#Exercise 2 :
    
inventory = {'apple': 20,
             'banana': 5,
             'orange': 0,
             'milk': 12,
             'bread': 0}

def check_inventory(inventory) :
    """
    This function receives a dictionary of products and their stock.
    It separates the product names into two lists :
    1. Products that are available.
    2. Products that are not available.

    Parameters
    ----------
    inventory : TYPE, dict
        A dictionary containing product names and their stock.

    Returns
    -------
    available_products : TYPE, list
        The names of products with stock greater than zero.

    unavailable_products : TYPE, list
        The names of products with zero stock.
    """

    available_products = []
    unavailable_products = []
    
    for product,stock in inventory.items() :
        if stock > 0 :
            available_products.append(product)
        else :
            unavailable_products.append(product)
            
    return available_products, unavailable_products

available, unavailable = check_inventory(inventory)

print('Available products : ' , available)
print('Unavailable products : ' , unavailable)
