#8_count_letter***

#1.count_letter_with_for :

def count_letter_with_for(word , letter) :
    '''
    in tabe do vorodi migirad (kalame/word va harf/letter)
    baresi mikonad ke harf chandbar dar kalame vojod darad.(ba estefade az halgheye for)
    '''
    
    count = 0
    
    for character in word :
        if character == letter :
            count = count + 1        
    return count

user_word = input('Enter a word : ').strip().lower()
user_letter = input('Enter a letter : ').strip().lower()

result = count_letter_with_for(user_word , user_letter)
print(result)

#2.count_letter_without_for :

def count_letter(word , letter) :
    '''
    in tabe do vorodi migirad (kalame/word va harf/letter)
    baresi mikonad ke harf chandbar dar kalame vojod darad.(bedone estefade az halgheye for)
    '''
    count = 0
    index = 0
    while True :
        if index == len(word) :
            break
        if word[index] == letter :
            count = count + 1
        index = index + 1
    return count

user_word = input('Enter a word : ').strip().lower()
user_letter = input('Enter a letter : ').strip().lower()

result = count_letter(user_word , user_letter)
print(result)