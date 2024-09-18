''' 1002 Common Characters '''

def commonChars(words):
    result = []
    selected = words[0]
    for i in range(len(selected)):
        for word in words:
            flag = False
            if selected[i] in word:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            result.append(selected[i])
    print('Result Word: ',result)





commonChars(words = ["bella","label","roller"])   ### ["e","l","l"]
commonChars(words = ["cool","lock","cook"])   #### ["c","o"]
