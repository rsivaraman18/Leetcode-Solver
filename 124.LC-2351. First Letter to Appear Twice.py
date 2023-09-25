'''2351. First Letter to Appear Twice'''

'''
Input: s = "abccbaacz"
Output: "c"
'''
'''
Input: s = "abcdd"
Output: "d"
'''

def twice(s):
    new = []
    
    for i in s:
        if i not in new:
            new.append(i)
            
        else:    
            print(i)
            break
        




twice("abccbaacz")
