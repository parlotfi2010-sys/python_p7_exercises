#13_countdown

def countdown(number) :
    '''
    yek adad daryaft mikone va makose on ada ro ta 0 pish mire.
    '''
    
    if number < 0 :
        return'Enter a positive number.'
        
    while number >= 0 :
        print(number)
        number = number - 1
    
user_number = input('Enter a number : ').strip()
if user_number.isdigit() :
    user_number = int(user_number)

countdown(user_number)