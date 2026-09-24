#14_multiplication_table

def multiplication_table(number) :
    '''
    yek adad daryaft mikonad va jadval zarb an adad az 1 ta 10 ra chap mikonad,
    '''
    
    for multiplier in range (1,11) :
        result = number * multiplier
        print (number , '*' , multiplier , '=' , result)

user_number = input('Enter a number : ').strip()
if user_number.isdigit() :
    user_number = int(user_number)
    
    multiplication_table(user_number)
else :
    print('Enter only a positive number.')