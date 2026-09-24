#15_check_stock

def check_stock(products , product_name) :
    '''
    bool
    in tabe do vorodi daryaft mikonad. yek dictionary shamele mahsolat va name mahsol.
    agar mojodi an mahsol 0 nabashad ---> True
    agar mojodi an mahsol 0 bashad   ---> False
    '''
    
    if product_name in products :        
        if products[product_name] != 0 :
            return True        
        else :
            return False     
    else :
        return False
    
products = {'iphone':5,
            'macbook':2,
            'airpods':0 }
product_name = input('Enter a product name : ').strip().lower()

result = check_stock(products , product_name)
print(result)

