''' 345. Reverse Vowels of a String '''

def rev_string(s):
    out =''
    pattern = ''
    vowels = 'AEIOUaeiou'
    for letter in s:
        if letter in vowels:
            pattern += letter
    print(pattern)       
    for letter in s:
        if letter in vowels:
            letter = pattern[-1]
            pattern = pattern[:-1]
            out = out + letter
        else:
            out = out + letter
    return(out)
            
        
rev_string('hello')
rev_string("leetcode")

