# ()
''' 1974. Minimum Time to Type Word Using Special Typewriter '''

def specialtype(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in range(0,len(word)):
        if i ==0:
            init    = 0
            reqmove = alpha.find(word[i])
            d1 = abs(reqmove-init)
            d2 = abs(26-d1)
            move = d1 if (d1<d2) else d2
            print(move)
            count = count + int(move+1)
            
        else:
            init = reqmove
            reqmove = alpha.find(word[i])
            d1 = abs(reqmove-init)
            d2 = abs(26-d1)
            move = d1 if (d1<d2) else d2
            print(move)
            count = count + int(move+1)
    print('Count total',count)
            
        
    
specialtype("abc")
specialtype("bza")
specialtype("zjpc")




'''
Input: word = "abc"
Output: 5
Explanation: 
The characters are printed as follows:
- Type the character 'a' in 1 second since the pointer is initially on 'a'.
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer clockwise to 'c' in 1 second.
- Type the character 'c' in 1 second.
'''

'''
Input: word = "bza"
Output: 7
Explanation:
The characters are printed as follows:
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer counterclockwise to 'z' in 2 seconds.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'a' in 1 second.
- Type the character 'a' in 1 second.
'''


'''
Input: word = "zjpc"
Output: 34
Explanation:
The characters are printed as follows:
- Move the pointer counterclockwise to 'z' in 1 second.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'j' in 10 seconds.
- Type the character 'j' in 1 second.
- Move the pointer clockwise to 'p' in 6 seconds.
- Type the character 'p' in 1 second.
- Move the pointer counterclockwise to 'c' in 13 seconds.
- Type the character 'c' in 1 second.
'''

















