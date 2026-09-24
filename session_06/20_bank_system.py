#20_bnak_system

accounts = [ {  'username': 'ali',
                'password': '1234',
                'balance': 5000,
                'transactions': []  },
             {  'username': 'sara',
                'password': '5678',
                'balance': 8000,
                'transactions': []  }  ]


def find_account(accounts, username) :
    '''
    karbar ra ba username peyda mikone va barmigardanad
    agar karbar peyda nashe None mide
    '''
    
    for account in accounts :
        if account['username'] == username :
            return account
    return None


#1.login :

def login(accounts, username, password) :
    '''
    bool
    tabe dar hesab ha jost va jo mikone va username va password ro check mikone.
    agar username(name karbari) vojod nadasht ---> None
    agar username(name karbari) vojod dasht baresi mikone ke username va password
    ba etelaate hesab motabeghat darand ya na :
        agar etelaat sahih bood ---> True
        agar nabood ---> False
    '''
    
    account = find_account(accounts, username)
    
    if account is None :
        return None
    if account['password'] == password :
        return True
    else :
        return False
    
username = input('Enter username : ').lower().strip()
password = input('Enter password : ').strip()

result = login(accounts, username, password)
print(result)

#2.1.withdraw :
    
def withdraw(accounts, username, amount) :
    '''
    hesabkarbari va mablaghe morde nazar ra daryaft mikonad.
    va mablaghe morde nazar ra az mojodiye karbar kam mikone
    agagr mojodi kafi nabashad False ra barmigardanad
    '''
    
    for account in accounts :
        if account['username'] == username :
            
            if account['balance'] >= amount :
                account['balance'] = account['balance'] - amount
                return True           
            return False
        
    return False


amount = int(input('Enter withdrawal amount : '))
result = withdraw(accounts, 'ali', amount)

print(result)
print('Ali balance : ' , accounts[0]['balance'])
print('Ali transactions : ' , accounts[0]['transactions']) #khali mimanad chon tarakonesh anjam nemishavad

#2.2.withdraw_with_transaction :
    
def withdraw_with_transaction(accounts, username, amount) :
    '''
    hesabkarbari va mablaghe morde nazar ra daryaft mikonad.
    va mablaghe morde nazar ra az mojodiye karbar kam mikone va tarakonesh ra namayesh midehad
    agagr mojodi kafi nabashad False ra barmigardanad
    '''
    for account in accounts :
        if account['username'] == username :
            
            if account['balance'] >= amount :
                account['balance'] = account['balance'] - amount
                
                transaction = {   'bank transaction': 'withdraw',
                                  'amount': amount   }
                
                account['transactions'].append(transaction)
                return True
            
            return False
    return False

amount = int(input('Enter withdrawal amount : '))
result = withdraw_with_transaction(accounts, 'ali', amount)

print(result)
print('Ali balance : ' , accounts[0]['balance'])
print('Ali transactions : ' , accounts[0]['transactions'])

#3.1.deposit :
    
def deposit(accounts, username, amount) :
    '''
    hesabkarbari va mablaghe morde nazar ra daryaft mikonad.
    va mablaghe morde nazar ra be mojodiye karbar ezafe mikone
    '''
    
    for account in accounts :
        if account['username'] == username :
            account['balance'] = account['balance'] + amount
            return True
    return False

amount = int(input('Enter deposit amount : '))
result = deposit(accounts, 'ali', amount)

print(result)
print('Ali balance : ' , accounts[0]['balance'])
print('Ali transactions : ', accounts[0]['transactions']) #khali mimanad chon tarakonesh anjam nemishavad

#3.2.deposit_with_transaction :

def deposit_with_transaction(accounts, username, amount):
    '''
    hesabkarbari va mablaghe morde nazar ra daryaft mikonad.
    va mablaghe morde nazar ra be mojodiye karbar ezafe mikone
    va mablaghe varizi ra be transactions ezafe mikone.
    '''
    
    for account in accounts :
        if account['username'] == username :
            account['balance'] = account['balance'] + amount
            
            transaction = {   'bank transaction': 'deposit',
                              'amount': amount              }
            account['transactions'].append(transaction)
            return True
    return False

amount = int(input('Enter deposit amount : '))
result = deposit_with_transaction(accounts, 'ali', amount)

print(result)
print('Ali balance : ' , accounts[0]['balance'])
print('Ali transactions : ' , accounts[0]['transactions'])

#4.show_transactions :
    
def show_transactions(accounts, username):
    '''
    username ra daryaft mikone va list transactions marbot be an karbar ra barmigardanad.
    agar username nabood None ra barmigardanad.
    '''
    
    for account in accounts:
        if account['username'] == username:
            return account['transactions']
    return None
    
username = input('Enter username: ').lower().strip()
result = show_transactions(accounts, username)
print('Transactions : ', result)

#5.transfer :
    
def transfer(accounts, sender_username, receiver_username, amount) :
    '''
    mablaghe 1000(mablaghe morede nazar) ra az mojodye sender_username kam mikone
    mablaghe 1000(mablaghe morede nazar) ra be mojodye receiver_username ezafe mikone
    enteghal ra dar transactions hesab haye marbote sabt mikone.
    dar nahayat list be roz shode accounts ra barmigardanad.
    '''
    
    sender = None
    receiver = None
    
    for account in accounts :
        if account['username'] == sender_username :
            sender = account
        if account['username'] == receiver_username :
            receiver = account
    if sender is None or receiver is None :
        return False
    if sender['balance'] < amount :
        return False
    
    sender['balance'] = sender['balance'] - amount
    receiver['balance'] = receiver['balance'] + amount
    
    sender_transaction = {   'bank transaction': 'withdraw',
                             'to': receiver_username,
                             'amount': amount              }
        
    receiver_transaction = {   'bank transaction': 'deposit',
                               'from': sender_username,
                               'amount': amount              }
    
    sender['transactions'].append(sender_transaction)
    receiver['transactions'].append(receiver_transaction)
    
    return True

sender_username = input('Enter sender username : ').lower().strip()
receiver_username = input('Enter receiver username : ').lower().strip()
amount = input('Enter amount : ').strip()
if amount.isdigit() :
    amount = int(amount)
    
    result = transfer(accounts, sender_username, receiver_username, amount)
    print ('Transfer result : ' , result)
    print('Update account : ' , accounts)
    
else :
    print('Amount must contain only numbers.')

#5.get_balance :
    
def get_balance(account, currency='USD') :
    '''
    do vorodi daryaft mikone, yek hesab va vahede pol(be tore pishfarz"USD" hast)
    hesabe morede nazar ra peyda mikone va mojodye an ra barmigardanad.
    agar vahede pol "RIAl" bood meghdare mojodi ra dar nerkhe dollar zarb mikone.
    '''

    if currency.upper().strip() == 'USD' :
        return account['balance']
    elif currency.upper().strip() == 'RIAL' :
       return account['balance'] * 2500000
    else :
       return None
   
username = input('Enter username : ').lower().strip()
account = find_account(accounts, username)
if account is None :
    print(None)
else :
    currency = input('Enter currency : ').upper().strip()
    
    if currency == '' :
        result = get_balance(account)
    else :
        result= get_balance(account, currency)
    print ('Balance : ' , result)
        