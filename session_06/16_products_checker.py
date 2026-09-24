#16_products_checker

products = [    {'code': 'z1', 'name': 'zara cloth 121', 'price': 30},
                {'code': 'z2', 'name': 'zara shoes 100', 'price': 45},
                {'code': 'z3', 'name': 'zara cloth 451', "price": 35},
                {'code': 'z4', 'name': 'zara shoes 300', 'price': 55},
                {'code': 'z5', 'name': 'zara shoes 231', 'price': 60},
                {'code': 'z6', 'name': 'zara bag 400', 'price': 110},
                {'code': 'z7', 'name': 'zara bag 500', 'price': 95}   ]

#1.product_price :
    
def product_price(products , product_code) :
    '''
    do vorodi daryaft mikone, list mahsolat(products) va code mahsol(product_name)
    va ghaymat mahsol ra barmigadanad.
    '''
    
    for product in products :
        if product['code'] == product_code :
            return product['price']

#2.product_name :

def product_name(products , product_code):
    '''
    do vorodi daryaft mikone, list mahsolat(products) va code mahsol(product_name)
    va name mahsol ra barmigadanad.
    '''  
    
    for product in products :
        if product['code'] == product_code :
            return product['name']
        
#3.product_information :
    
def product_information(products , product_code):
    '''
    do vorodi daryaft mikone, list mahsolat(products) va code mahsol(product_name)
    va dar khoroji yek Tuple shamele etelaate mahsol ra barmigardanad.
    '''  

    for product in products :
        if product ['code'] == product_code :
            product_Information = ( product['code'],
                                    product['name'],
                                    product['price'] )
            return product_Information
        
code = input('Enter product code : ').strip().lower()

print('Product price : ' , product_price(products , code))
print('Product name : ' , product_name(products , code))
print('Product information : ' , product_information(products , code))