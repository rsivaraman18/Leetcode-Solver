## 2942 -- Find words Containing Characters

def findWordsContaining(words,x):
    val = []
    for i in range(len(words)):
        if x in words[i]:
            val.append(i)
    print('Value:',val)
    return val





findWordsContaining(words = ["leet","code"], x = "e")
findWordsContaining(["abc","bcd","aaaa","cbc"], x = "a")
findWordsContaining( words = ["abc","bcd","aaaa","cbc"], x = "z")