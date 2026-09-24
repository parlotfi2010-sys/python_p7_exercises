#2_check_number

#1.check_even_odd :

def check_even_odd(number) :
    '''
    tabe yek adad daryaf mikonad.
    moshakhas mikonad adad vared shode zoj(Even) hast ya fard(Odd)
    '''
    
    if number % 2 == 0 :
        return 'Even'
    else :
        return 'Odd'

number = input('Enter a number : ').strip()
if number.isdigit() :
    number = int(number)
    
    result = check_even_odd(number)
    print (result)
else :
    print('Enter only number.')

#2.is_even :

def is_even(number) :
    '''
    bool
    yek adad daryaft mikone.
    agar adad zoj(Even) bood ---> True
    agar adad fard(Odd) bood ---> False
    '''
    
    if number % 2 == 0 :
        return True
    else :
        return False
    
number = input('Enter a number : ').strip()
if number.isdigit() :
    number = int(number)
    
    result = is_even(number)
    print(result)
else :
    print('Enter only number.')

#3.check_sign :

def check_sign(number) :
    '''
    yek adad daryaft mikonad va barresi mikonad :
        agar adad + bood ---> Positive
        agar adad - bood ---> Negative
        agar 0 bood ---> Zero
    '''
    
    if number > 0 :
        return 'Positive'
    elif number < 0 :
        return 'Negative'
    else :
        return 'Zero'

number = input('Enter a number : ').strip()
if number.isdigit() or len(number) > 1 and number[0] in '-+' and number[1:] :#**
    number = int(number)
    
    result = check_sign(number)
    print(result)
else :
    print('Enter only number.')
