#3_check_age

def check_age(age) :
    '''
    yek tabe ke yek adad(sen/age) ra daryaft mikonad
    agar sen az 18 kamtar bashad migoyad dastresi rad shod
    va agar bishtar bashad migoyad khosh amadid.
    '''
    
    if age < 18 :
        return 'Access Denied.'
    else :
        return 'Welcome'

age = input('Enter your age : ').strip()
if age.isdigit() :
    age = int(age)
    
    result = check_age(age)
    print (result)
else :
    print ('Enter only number.')
