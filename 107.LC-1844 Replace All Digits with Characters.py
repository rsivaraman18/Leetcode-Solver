'''
pbm: 1844 Replace All Digits with Characters
Q1
s = "a1c1e1"     Output: "abcdef"
s = "a1b2c3d4e"  Output: "abbdcfdhe" 
'''
# ()

def replace(s):
    out = ''
    for letter in s:
        if letter.isalpha():
            x = letter
            out = out + x
        else:
            new = ord(x)+int(letter)
            new = chr(new)
            out = out + new
            
    print(out)
    



#replace("a1c1e1")
replace("a1b2c3d4e")
