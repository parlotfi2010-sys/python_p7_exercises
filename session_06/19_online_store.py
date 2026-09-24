#19_online_store***

products = [ {'code': 'p1', 'name': 'Keyboard', 'price': 50, 'stock': 4},
             {'code': 'p2', 'name': 'Mouse', 'price': 30, 'stock': 7},
             {'code': 'p3', 'name': 'Monitor', 'price': 250, 'stock': 2},
             {'code': 'p4', 'name': 'Headphone', 'price': 80, 'stock': 0}  ]

#1.find_product :
    
def find_product(products, code):
    '''
    in tabe code mahsol ra daryaft mikonad.
    agar mahsol peyda shod dictionary marbot be an mahsol ra barmigardanad.
    agar mahsol peyda nashod "None" ra bar migardanad.
    '''
    
    for product in products :
        if product['code'] == code :
            return product
    return None

product_code = input('Enter product code : ').lower().strip()
result = find_product(products, product_code)
print('Product : ', result)

#2.add_to_cart :
    
def add_to_cart(products, cart, code) :
    '''
    mahsol ra bar asas code peyda mikonad.
    agar mojodie mahsol bishtar az 0 bood an ra be sabad kharid(cart) ezafe mikonad
    va an ra barmigardanad.
    '''

    product = find_product(products, code)
    
    if product is not None and product['stock'] > 0 :
        cart.append(product)
    return cart

cart = []
product_code = input('Enter product code : ').lower().strip()
cart = add_to_cart(products, cart, product_code)
print('Cart : ' , cart)

#3.update_product_stock :
    
def update_product_stock(products, code) :   
    '''
    mahsol ra bar asas code peyda mikonad.
    agar mojodie mahsol bishtar az 0 bood az mojodye an yek adad kam mikonad
    va list beroz shode ra barmigardanad.
    '''
    
    product = find_product(products, code)
    
    if product is not None and product['stock'] > 0 :
        product['stock'] = product['stock'] - 1
    return products

product_code = input('Enter product code : ').lower().strip()
products = update_product_stock(products , product_code)
print('Updated products :' , products)

#4.buy_product :
    
def buy_product(products, cart, code) :
    '''
    mahsol ra bar asas code peyda mikonad.
    agar mojodie mahsol bishtar az 0 bood an ra be sabad kharid(cart) ezafe mikonad
    va az mojodye an yek adad kam mikonad.
    va list beriz shode ra barmigardanad.
    '''

    product = find_product(products, code)
    
    if product is not None and product['stock'] > 0 :
        cart.append(product)
        product['stock'] = product['stock'] - 1
    return cart, products

cart = []

product_code = input('Enter product code : ').lower().strip()
cart, products = buy_product(products, cart, product_code)
print('Cart :' , cart)
print('Updated products :' , products)
    