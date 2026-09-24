#Exercise 3 :

    
employees = {'E01': {'name': 'Ali',
                     'age': 28,
                     'salary': 3000},
             'E02': {'name': 'Sara',
                     'age': 32,
                     'salary': 4500},
             'E03': {'name': 'Reza',
                     'age': 25,
                     'salary': 2800}}
#3.1.highest_salary_employee :

def highest_salary_employee(employees) :
    """
    This function receives a dictionary of employees
    and returns the name of the employee with the highest salary.

    Parameters
    ----------
    employees : TYPE, dict
        Dictionary of employees and their information.

    Returns
    -------
    employee_name : TYPE, str
        Name of the employee with the highest salary.
    """
    
    first_employee = list(employees.values())[0]
    highest_salary = first_employee['salary']
    employee_name = first_employee['name']
    
    for information in employees.values() : 
        if information['salary'] > highest_salary :
            highest_salary = information['salary']
            employee_name = information['name']
    return employee_name

result = highest_salary_employee(employees)
print('Highest salary employee : ' , result)

#3.2.lowest_salary_employee :

def lowest_salary_employee(employees) :
    """
    This function receives a dictionary of employees
    and returns the name of the employee with the lowest salary.

    Parameters
    ----------
    employees : TYPE, dict
        Dictionary of employees and their information.

    Returns
    -------
    employee_name : TYPE, str
        Name of the employee with the lowest salary.
    """

    first_employee = list(employees.values())[0]
    lowest_salary = first_employee['salary']
    employee_name = first_employee['name']
    
    for information in employees.values() :
        if information['salary'] < lowest_salary :
            lowest_salary = information['salary']
            employee_name = information['name']
    return employee_name

result = lowest_salary_employee(employees)
print('Lowest salary employee : ' , result)

#3.3.salary_above_3000 :

def salary_above_3000(employees) :
    """
    This function receives a dictionary of employees
    and returns a list containing the names of employees
    whose salaries are greater than 3000.

    Parameters
    ----------
    employees : TYPE, dict
        Dictionary of employees and their information.

    Returns
    -------
    employee_names : TYPE, list
        Names of employees whose salaries are above 3000.
    """

    employee_names = []
    
    for information in employees.values() :
        if information['salary'] > 3000 :
            employee_names.append(information['name'])
    return employee_names

result = salary_above_3000(employees)
print('Employees with salaries above 3000 : ' , result)

#3.4.employees_above_salary :

def employees_above_salary(employees, amount) :
    """
    This function receives an employees dictionary and a amount.
    It returns the names of employees whose salaries
    are greater than the given amount.

    Parameters
    ----------
    employees : TYPE, dict
        Dictionary of employees and their information.
    number : TYPE, int
        Salary amount used for comparison.

    Returns
    -------
    employee_names : TYPE, list
        Names of employees whose salaries are greater than the given amount.
    """
    
    employee_names = []
    
    for information in employees.values() :
        if information['salary'] > amount :
            employee_names.append(information['name'])
    return employee_names

user_amount = input('Enter your amount : ').strip()
if user_amount.isdigit() :
    user_amount = int(user_amount)
    
    result = employees_above_salary(employees, user_amount)
    print ('Employees : ' , result)
    
else :
    raise ValueError('Your amount must contain only numbers')
    
#3.5.average_salary :
    
def average_salary(employees) :
    """
    This function receives a dictionary of employees
    and returns the average of all salaries.

    Parameters
    ----------
    employees : TYPE, dict
        Dictionary of employees and their information.

    Returns
    -------
    average : TYPE, float
        Average salary of all employees.
    """
    
    total = 0
    count = 0
    
    for information in employees.values() :
        total = total + information['salary']
        count = count + 1
    average = total / count
    return average

result = average_salary(employees)
print('Average salary : ' , result)
    
