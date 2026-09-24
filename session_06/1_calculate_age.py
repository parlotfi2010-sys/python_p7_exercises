#1_calculate_age

#1.calculate_age :

def calculate_age(birth_year):
    '''
    yek tabe ke sal tavalod fard ro daryaft mikone
    va sen fard ro mohasede mikone.
    '''
    
    current_year = 2026
    age = current_year - birth_year 
    return age

year = int(input('Enter your year of birth : '))

result = calculate_age (year)
print('Your age : ' , result)

#2.calculate_age_by_type :

def calculate_age_by_type (birth_year , date_type):
    '''
    yek tabe ke do vorodi daryaft mikone. sale tavalod va noee tarikh
    agar noee tarikh shamsi bashad sen ra bar asas 1405 mohasebe mikonad
    agar noee tarikh miladi bashad sen ra bar asas 2026 mohasebe mikonad.
    '''
    
    if date_type.lower().strip() == 'miladi' :
        age = 2026 - birth_year
        return age #
    elif date_type.lower().strip() == 'shamsi' :
        age = 1405 - birth_year
        return age #
    else :
        return 'The date_type is incorrect'
        #raise ValueError('')
    #return sen

Year = int(input('Enter your year of birth : '))
Type = input('Enter your type of dete (miladi/shamsi) : ')

result = calculate_age_by_type(Year , Type)
print('Your age : ' , result)

#3.calculate_age_default :
    
def calculate_age_default(birth_year , date_type='miladi'):
    '''
    yek tabe ke do vorodi daryaft mikonad. sale tavalod va noee tarikh.
    agar noee tarikh shamsi bashad sen ra bar asas 1405 mohasebe mikonad
    agar noee tarikh miladi bashad sen ra bar asas 2026 mohasebe mikonad.
    agar noee tarikh vared nashavad be tor pishfarz an ra miladi hesab mikonad.   
    '''
    
    if date_type.lower().strip() == 'miladi' :
        age = 2026 - birth_year
        return age
    elif date_type.lower().strip() == 'shamsi' :
        age = 1405 - birth_year
        return age
    else :
        return 'The date_type is incorrect'

Year = input('Enter your year of birth : ').strip()
if Year.isdigit() : 
    Year = int(Year)
    
    Type = input('Enter your type of dete (miladi/shamsi) : ')
    if Type == ''.strip() :
        result = calculate_age_default(Year)
    else :
        result = calculate_age_default(Year , Type)
        
    print('Your age : ' , result)

else :
    print('Birth year must contain only numbers.')

#4.calculate_age_auto :
    
def calculate_age_auto(birth_year) :
    '''
    yek tabe ke yek vorodi daryaft mikonad. tarikh sale tavalod.
    va tashkhis midehad ke tarikhi ke karbar vared karde shamsi hast ya miladi,
    va sen ra hesab mikonad.
    '''
    
    if 1200 <= birth_year <= 1405 :
        age = 1405 - birth_year
        return f'Your year of birth is "shamsi" and your age is {age}'
    elif 1800 <= birth_year <= 2026 :
        age = 2026 - birth_year
        return f'Your year of birth is "miladi" and your age is {age}'
    else :
        return 'Invalid birth year.'
    
year = input('Enter your year of birth : ').strip()
if year.isdigit() :
    year = int(year)

    result = calculate_age_auto(year)
    print('Your age : ' , result)
else :
    print('Birth year must contain only numbers.')
        