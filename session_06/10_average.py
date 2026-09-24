#10_average

def calculate_average(scores) :
    '''
    in tabe yek list az nomarat ra daryaft mikonad va miyangin momarat ra hesab mikonad.
    '''
    
    if len(scores) == 0 :
        return 'The list is empty.'
    
    total = 0
    for score in scores :
        total = total + score
        
    average = total / len(scores)
    
    return average

score_list = input('Enter scores : ').split()
for index in range(len(score_list)) :
    score_list[index] = float(score_list[index])

result = calculate_average(score_list)
print('The average : ' , result)