#11_failed_score

def failed_score(scores) :
    '''
    yek list nomarat ra be onvan vorodi daryaft mikonad.
    nomarate mardod(zire 10) ra hazf mikonad va lis jadid ra barmigardanad.
    '''
    
    if len(scores) == 0 :
        return 'The list is empty.'
    
    failed_scores = []
    
    for score in scores :
        if score >= 10 :
            failed_scores.append(score)
    return failed_scores

scores = [18, 7, 12, 9, 10, 5, 16]
result = failed_score(scores)
print(result)