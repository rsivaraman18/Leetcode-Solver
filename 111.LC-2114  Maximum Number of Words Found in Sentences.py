'''
Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
'''

# ()

def cword(sentences):
    slen = len(sentences)
    print(slen)
    mylist = []
    for i in range(0,slen):
        new = sentences[i].split()
        new = len(new)
        mylist.append(new)
    print(mylist)
    maxword = max(mylist)
    print(maxword)
        
def sen():
    sent =  ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    d = set()
    for item in sent:
        temp = item.split(' ')  
        d.add(len(temp))
    print(d)
    maxletter = max(d)
    print(maxletter)

sen()      
        



w1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
cword(w1)
