#6_check_email

def check_email(email):
    '''
    bool
    yek vorodi(email) daryaft mikonad va an ra barresi mikonad :
        @ va .com dashte bashad va fasele nabashad.
    va agar motabar bood ---> True
    agar na              ---> False
    '''
    
    email = email.lower()
    if ' ' not in email and '@' in email and '.com' in email :
        return True
    else :
        return False

user_email = input('Enter your email : ')

result = check_email(user_email)
print(result)