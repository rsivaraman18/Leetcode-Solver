'''
pbm 2000 -Reverse Prefix of word 
word = "abcd efd", ch = "d"
out  = "dcba efd"
'''

def word(word,ch):
    wlen = len(word)
    ind = 0
    for i in range(0,wlen):
        if (word[i]==ch):
            ind = i
            break
        
    new1 = word[0:ind+1]
    new1 = new1[::-1]
    print(new1)
    new2 = word[ind+1:wlen]
    out  = new1 + new2

    #return(out)
    print(out)
        

word("abcdefd","d")

