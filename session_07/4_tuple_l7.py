#exercise 4 :

sales = (('Ali', 'Laptop', 1200),
         ('Sara', 'Phone', 800),
         ('Ali', 'Phone', 800),
         ('Reza', 'Laptop', 1200),
         ('Sara', 'Laptop', 1200),
         ('Ali', 'Mouse', 50))

#4.1.total_purchase :
    
def total_purchase(sales) :
    """
    This function receives sales information
    and returns the total purchase of each customer.
    
    
    Parameters
    ----------
    sales : TYPE, tuple
        This function receives sales information and
        returns the total purchase of each customer.

    Returns
    -------
    customer_totals : TYPE, dict
        Customer names and their total purchase.
    """
    
    customer_totals = {}
    
    for customer, product, price in sales :
        if customer in customer_totals :
            customer_totals[customer] = (customer_totals[customer] + price)
        else :
            customer_totals[customer] = price           
    return customer_totals

result = total_purchase(sales)
print('Customer totals : ' , result)

#4.2.product_sales_count :
    
def product_sales_count(sales) :
    """
    This function receives sales information
    and returns the number of sales for each product.

    Parameters
    ----------
    sales : tuple
        Sales information containing customer name,
        product name and price.

    Returns
    -------
    product_counts : dict
        Product names and their sales count.
    """
    
    product_counts = {}
    
    for customer, product, price in sales :
        if product in product_counts :
            product_counts[product] = (product_counts[product] + 1)
        else:
            product_counts[product] = 1
    return product_counts

result = product_sales_count(sales)
print('Product sales count : ' , result)

#4.3.total_store_income :
    
def total_store_income(sales):
    """
    This function receives sales information
    and returns the total income of the store.

    Parameters
    ----------
    sales : tuple
        Sales information containing customer name,
        product name and price.

    Returns
    -------
    total_income : int
        Total income of the store.
    """

    total_income = 0

    for customer, product, price in sales :
        total_income = total_income + price
    return total_income

result = total_store_income(sales)
print('Total store income : ' , result)
