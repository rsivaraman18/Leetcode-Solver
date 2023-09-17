'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''
# ()
# print()

# ********************************************************

def roman_try():
    s = 'MCMXCIV' #1994
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    le = len(s) 
    ans = 0
    for i in range (0,le):
        if ( (i+1)!= len(s)) and ( d[s[i]] < d[s[i+1]] ):
            ans = ans - d[s[i]]
        else:
            ans = ans + d[s[i]]
    return ans
    
print(roman_try())

# ********************************************************

class Solution:
    def romanToInt(self, s: str) -> int:
        s=s
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        le = len(s) 
        ans = 0
        for i in range (0,le):
            if ( (i+1)!= len(s)) and ( d[s[i]] < d[s[i+1]] ):
                ans = ans - d[s[i]]
            else:
                ans = ans + d[s[i]]
        return ans





# *******************************************************

























'''
def roman(s):
    roman = s
    num = 0
    le =len(roman)
    for i in range(0,(le)):
        new_rom = roman[i]
        if (new_rom=='I'):
            value = 1
            num = num + value
            
        elif (new_rom=='V'):
            value = 5
            num = num + value
            
        elif (new_rom=='X'):
            value = 10
            num = num + value
            
        elif (new_rom=='L'):
            value = 50
            num = num + value
            
        elif (new_rom=='C'):
            value = 100
            num = num + value
        elif (new_rom=='D'):
            value = 500
            num = num + value
            
        elif (new_rom=='M'):
            value = 1000
            num = num + value
        else:
            print('Siva error')
    return num


print(roman( "LVIII"))
print(roman( "MCMXCIV"))
print(roman( 'XI'))
            
 '''       
