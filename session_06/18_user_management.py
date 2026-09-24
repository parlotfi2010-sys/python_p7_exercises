#18_user_management

users = [ { 'username': 'ali',
            'age': 25,
            'city': 'Tehran',
            'active': True  },
         { 'username': 'sara',
           'age': 17,
           'city': 'Tabriz',
           'active': True  } ]

#1.add_user :
    
def add_user(users , username , age , city) :
    '''
    yek karbar jadid misazad va be list ezafe mikonad.
    meghdare active ra be sorate pishfarz True gharar midehad
    va dar nahayat list beroz shdeye karbaran ra barmigardanand.
    '''
    
    new_user = { 'username': username,
                 'age': age,
                 'city': city,
                 'active': True  }
    users.append(new_user)
    return users

username = input('Enter username : ').strip().lower()
age = input('Enter age : ').strip()
city = input('Enter city : ').strip().lower()
if age.isdigit() :
    age = int(age)
    
    updated_users = add_user(users , username , age , city)
    print('Updated users : ' , updated_users )

else:
    print('Age must be a number.')
    
#2.find_user :

def find_user(users , username) :
    '''
    dar list jostojo mikonad va karbar morede nazar ra peyda mikonad.
    agar karbar vojod nadasht "None" ra barmigardanad.
    agar karbar vojod dasht, dictionary marbot be haman karbar ra barmigardanad.
    '''
    
    for user in users :
        if user['username'] == username :
            return user
    return None

searched_username = input('Enter username to find : ').lower().strip()
result = find_user(users , searched_username)
print('Found user : ' , result)

#3.check_access(users , username)

def check_access(users , username) :
    '''
    bool
    karbare morede nazar ra petda mikonad :
        sen karbar hadaghal 18 bashad.
        active karbar True(faal) bashad
    agar hado shart bood ---> True
    agar na              ---> False
    '''

    user = find_user(users, username)
    
    if user is None :
        return False
    elif user['age'] >= 18 and user['active'] == True :
        return True
    else :
        return False

access_username = input('Enter username to check access : ').lower().strip()
result = check_access(users , access_username)
print(result)

#4.get_adult_users :
    
def get_adult_users(user) :
    '''
    karbarani ke az 18 sal be bala hastand ra az list joda mikonad
    va an list ra barmigardanad.
    '''
    
    adult_users = []
    
    for user in users :
        if user['age'] >= 18 :
            adult_users.append(user)
    return adult_users

result = get_adult_users(users)
print('Adult users :' , result)