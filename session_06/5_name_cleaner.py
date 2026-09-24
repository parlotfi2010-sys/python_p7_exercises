#5_name_cleaner

def name_cleaner(full_name):
    '''
    yek tabe ke esm kamel fard(full name) yani nam(name) va nam khanevadegi(last name)
    ra daryaft mikonad va an ra moratab shode tahvil midehad.
    fasele haye ezafi ra hazf mikonad va horof ra be shekle sahih minevisad.
    '''
    
    full_name =' '.join(full_name.split())
    full_name = full_name.title()
    return full_name

name = input('Enter your full name : ')

result = name_cleaner(name)
print('Corrected name : ' , result)