#17_Menu_app

def Menu_app() :
    '''
    vorodi nadarad.
    yek menu namayesh midehad va sefaresh haye moshtari ra sabt mikonad.
    daryaft sefaresh ta zamani edame darad ke karbar kalame "order" ra vared konad.
    dar payan list sefaresh ha bargardande mishavad.
    '''
    
    menu = ['pizza' , 'burger' , 'sandwich' , 'salad']
    orders = []
    
    print ('Food Menu : ')
    for food in menu :
        print('- ' , food)
        
    print('Enter "order" to finish your order.')
    
    while True :
        user_order = input('Choose a food : ').strip().lower()
    
        if user_order == 'order':
            break
        elif user_order in menu :
            orders.append(user_order)
            print(f'{user_order} added to your order.')
        else :
            print('This food is not available.')
            
    return orders

customer_orders = Menu_app()
print('Your orders : ' , customer_orders)