#12_calculator

def calculator(number1 , number2 , operation) :
    '''
    se vorodi daryaft mikone va amaliyate gofte shode ra roye adad ha emal mikone.
    jam(+) ya tafrigh(-) ya zarb(*) ya taghsim(/)
    agar hichkodam nabood ---> None
    '''
    
    if operation == '+' :
        return number1 + number2
    elif operation == '-' :
        return number1 - number2
    elif operation == '*' :
        return number1 * number2
    elif operation == '/' :
        if number2 == 0 :
            return 'Null'
        return number1 / number2
    else :
        return 'None, , choose from + or - or * or /.'
    
first_number = input('Enter first number : ').strip()
if first_number.isdigit() :
    first_number = float(first_number)
    
second_number = input('Enter second number : ').strip()
if second_number.isdigit() :
    second_number = float(second_number)

user_operation = input('Enter an operation : ').strip()

result = calculator(first_number, second_number, user_operation)
print(result)
