 #9_find_max

def find_max(numbers) :
    '''
    in tabe yek list az adad daryaft mikonad va bozorgtarin ada ra peyda mikonad.
    '''
    if len(numbers) == 0 :
        return 'The list is empty'
    maximum = numbers[0]
    for number in numbers :
        if number > maximum :
            maximum = number
    return maximum

number_list = input('Enter your numbers : ').split()
for index in range(len(number_list)) :
    number_list[index] = int(number_list[index])
    
result = find_max(number_list)
print('max number : ' , result)