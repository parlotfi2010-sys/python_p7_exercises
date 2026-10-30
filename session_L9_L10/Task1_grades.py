#==================================
#==============Task 1==============
#==================================

def read_all_grades() :

    grades = []
   
    try :
        with open('grades.txt', 'r', encoding='utf-8') as file :
            for line in file :
                line = line.strip()
                
                if line == '' :
                    continue
                    
                try :
                    name, grade = line.split(',')
                    grade = float(grade)
                    grades.append([name, grade])
                    
                except(ValueError, TypeError) :
                    print(f'Error reading this line : {line}')

                    
    except FileNotFoundError :
        pass
    
    except OSError as error :
        print(f'Error opening file : {error}')

    return grades


def save_grades(grades) :
    """
    Save all grades to file.

    Parameters
    ----------
    grades : TYPE, float

    Returns
    -------
    
    """

    try :
        with open('grades.txt', 'w', encoding='utf-8') as file :
            for student in grades :
                file.write(f'{student[0]},{student[1]}\n')            
        return True
    
    except OSError as error :
        print(f'Error saving file : {error}')
        return False


def add_grade(name:str , grade:float) :
    """
    Get the student's name and grade and save them to a file.

    Parameters
    ----------
    name : str
        First input.
        grade : float
        Second input
        
    Returns
    -------
    None
    """

    
    if not isinstance(name, str) :
        print('Error : Student name must be a string.')
        return
    
    name = name.strip()
    
    if name == '' or ',' in name :
        print('Error : Invalid student name.')
        return
    
    try :
        grade = float(grade)

    except(ValueError, TypeError) :
        print('Error : Grade must be a number.')
        return
    
    if grade < 0 or grade > 20 :
        print('Error : Grade must be between 0 and 20.')
        return
    
    grades = read_all_grades()

    for student in grades :
        if student[0].lower() == name.lower() :
            student[1] = grade
            
            if save_grades(grades) :
                print(f'Grade for {name} has been updated.') 
                
            return

    grades.append([name, grade])

    if save_grades(grades) :
        print(f'Grade for {name} has been successfully recorded.')
        
        
def read_grades() :
    """
    Displaying recorded grades.

    Returns
    -------
    Returns a list of grades.
    """

    grades = read_all_grades()

    if len(grades) == 0 :
        print('No grades have been recorded yet.')
        return
    
    print('Students grades list : \n')
    
    for student in grades :
        print(f'Name: {student[0]} , Grade: {student[1]}')
        

def calculate_avarage() :
    """
    Calculating the avarage grades.

    Returns
    -------
    None
    """
    
    grades = read_all_grades()

    if len(grades) == 0 :
        print('No grades available to calculate the avarage.')
        return
    
    total = 0

    for student in grades :
        total += student[1]
        
    avarage = total / len(grades)
    print(f'Class avarage : {avarage:.2f}')
    
    
def find_top_student() :
    """
    Finding thث top student.

    Returns
    -------
    Returns the name of top student.
    """

    grades = read_all_grades()

    if len(grades) == 0 :
        print('No student available to check.')
        return

    top_student = grades[0]

    for student in grades :
        if student[1] > top_student[1] :
            top_student = student
            
    print(f'The highest grade belongs to {top_student[0]} with a grade of {top_student[1]}')

        
#==================================
#==================================
#==================================

print('Testing valid grade entries : \n')
add_grade('Ali', 18.5)
add_grade('Sara', 16)
add_grade('Reza', 19.25)

print('testing non numeric grades : \n')
add_grade('Maryam', 'A')

print('Testing grades above 20 : \n')
add_grade('Hasan', 21)

print('Testing negative grades : \n')
add_grade('Nima', -1)

print('Testing emptu names : \n')
add_grade('   ', 17)

print('Testing grade updates for existing students : \n')
add_grade('Ali', 19.5)

print('Testing non-string name : \n')
add_grade(123, 15)

print('Testing invalid grade type : \n')
add_grade('Mina', None)

print('Displaying grades : \n')
read_grades()

print('Calculating grades : \n')
calculate_avarage()

print('Finding the top student : \n')
find_top_student()

    