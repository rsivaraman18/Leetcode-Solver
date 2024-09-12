''' 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence  '''

''' Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4  '''

def find_word(sentence,searchWord):
    sent = sentence.split(' ')
    
    for i in range(len(sent )):
        if sent [i].startswith(searchWord):
            print( i+1)
    return(-1)
    


find_word("i love eating burg" , 'burg')
find_word("i am tired", searchWord = "you" )
