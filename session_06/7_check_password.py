#7_check_password ***

#1.check_password :
    
def check_password(password) :
    '''
    ramze obor(password) ra daryaft mikonad va baresi mikonad.
    agar hadaghal 8 character va yek adad va yek harf dasht ---> password sabt shod
    agar sharayet ra nadasht ---> password kamel nist.
    '''
    
    has_number = False
    has_alphabet = False
    
    for character in password :
        if character.isdigit() :
            has_number = True
        if character.isalpha() :
            has_alphabet = True
            
    if len(password) >= 8 and has_number and has_alphabet :
        return 'Password has been registered.'
    else :
        return 'Password is incomplete.'
    
user_password = input('Enter your password : ')
print(check_password(user_password))

#2.is_valid_password :
    
def is_valid_password(password):
    '''
    bool
    ramze obor(password) ra daryaft mikonad va baresi mikonad.
    agar hadaghal 8 character va yek adad va yek harf dasht ---> True
    agar sharayet ra nadasht                                ---> False
    '''
    
    has_number = False
    has_alphabet = False
    
    for character in password :
        if character.isdigit() :
            has_number = True
        if character.isalpha() :
            has_alphabet = True
            
    if len(password) >= 8 and has_number and has_alphabet :
        return True
    else :
        return False
    
user_password = input('Enter your password : ')
print(is_valid_password(user_password))

#3.check_password_strength :

def check_password_strength(password) :
    '''
    in tabe ghodrate password ra baresi mikonad az bein 1 ta 4 :
        4 --> bishtar az 8 character va shamel har, adad, haf bozorg va harf kochak.
        3 --> bishtar az 8 character va shamel harf va adad.
        2 --> bishtar az 8 character.
        1 --> kamtar az 8 character.
    '''
    
    has_number = False
    has_alphabet = False
    has_uppercase = False
    has_lowercase = False
    
    for character in password :
        if character.isdigit() :
            has_number = True
        if character.isalpha() :
            has_alphabet = True
        if character.isupper() :
            has_uppercase = True
        if character.islower() :
            has_lowercase = True
    if len(password) >= 8 and has_number and has_alphabet and has_uppercase and has_lowercase :
        return 4
    elif len(password) >= 8 and has_number and has_alphabet :
        return 3
    elif len(password) >= 8 :
        return 2
    else :
        return 1

user_password = input('Enter your password : ')

result = check_password_strength(user_password)
print('Password strength : ' , result)