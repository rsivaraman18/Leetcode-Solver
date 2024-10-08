'''1374. Generate a String With Characters That Have Odd Counts'''

def oddword(n):
    out = ''
    
    if n%2==0:
        letter = chr(97)*(n-1)
        out = out + letter
        letter2 = chr(97+1)
        out = out + letter2
        
    else:
        letter = chr(97)*(n)
        out = out + letter
    
    print(out)
            
       
oddword(n=4)
oddword(n=5)














'''
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  
'''

'''
Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
'''

'''
Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
'''

'''
Input: n = 7
Output: "holasss"
'''
