''' 2490. Circular Sentence '''

def isCircularSentence(sentence):
    sent = sentence.split()
    flag = []
    for i in range(len(sent)):
        if i!=len(sent)-1:
            if sent[i][-1]==sent[i+1][0]:
                flag.append(True)
            else:
                flag.append(False)
        else:
            if sent[0][0]==sent[-1][-1]:
                flag.append(True)
            else:
                flag.append(False)


    result = all(flag)
    print('Result :',result)

    if result:
        return True
    else:
        return False


isCircularSentence( "leetcode exercises sound delightful") # t
isCircularSentence("eetcode") # t
isCircularSentence( "Leetcode is cool") # f

isCircularSentence("MuFoevIXCZzrpXeRmTssj lYSW U jM") #f