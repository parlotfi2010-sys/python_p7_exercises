#Optional 3_l8 :
    
def create_profile(name, age, **kwargs) :
    '''
    It takes all user information
    and can add new information to user profile.

    Parameters
    ----------
    name : TYPE, str
        The user name.
    age : TYPE, int
        The user age.
    **kwargs : TYPE
        Additional user information.

    Returns
    -------
    profile : TYPE, dict
        All user information in dictionary.
    '''
    
    print(f'name : {name} ')
    print(f'age : {age} ')
    print()
    print('Other Information : ')
    for key, value in kwargs.items() :
        print(f'{key} : {value} ')
    print()
    print(f'Length of other information : {len(kwargs)}')
    if 'city' in kwargs :
        print(f'city : {kwargs["city"]}')        
    if 'email' not in kwargs:
        print('Email not found.')
    profile = {'name' : name,
               'age' : age}

    profile.update(kwargs)
    return profile
    
create_profile('Ali' , 30 , city='Tehran' , job='Artist', email='ali.d30@gmail.com')   

