# ( )
'''
344 Reverse of letter in string
Q1 - inp1 -["h","e","l","l","o"]  out1-  ["o","l","l","e","h"]
'''

def reverse(s):
    list1 = []
    for i in range(len(s)-1,-1,-1):
        new = s[i]
        list1.append(new)
    print(list1)
        

def reverse1 (s):
    s.sort(reverse=True)

    print(s)
    
def reverse2(s):
    rev = s[::-1]
    print(rev)



reverse( ["h","e","l","l","o"])
#reverse( ["H","a","n","n","a","h"] )

reverse1( ["h","e","l","l","o"])
reverse2(["h","e","l","l","o"])
