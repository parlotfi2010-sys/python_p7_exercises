#4_caculate_grade

def calculate_grade(score):
    '''
    yek vorodi (nomre/score) daryaft mikonad va mesle yek systeme nomredehi amal mikonad.
    90 ta 100    ---> A
    80 ta 89     ---> B
    70 ta 79     ---> C
    60 ta 69     ---> D
    kamtar az 60 ---> F
    '''
    
    if 90 <= score <= 100 :
        return 'A'
    elif 80 <= score < 90 :
        return 'B'
    elif 70 <= score < 80 :
        return 'C'
    elif 60 <= score < 70 :
        return 'D'
    elif 0 <= score < 60 :
        return 'F'
    else :
        return'Score must be between 0 and 100.'
        
score = input('Enter your score : ').strip()
if score.isdigit() :
    score = int(score)
    
    result = calculate_grade(score)
    print('Your grade : ' , result)
else :
    print('Enter only number.')