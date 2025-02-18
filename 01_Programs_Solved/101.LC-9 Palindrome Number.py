print('Program to find Palindrome in Leet code')
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        rev = temp[::-1]
        #print(rev)

        if (temp == rev):
            return True
        else:
            return False
 
#********************************************************
        
def pal(x):
    temp = str(x)
    rev = temp[::-1]
    print('Given',x)
    
    print('REv',rev)

    if (temp == rev):
        return 'true'
    else:
        #print('x',x)
        #print('rev',rev)
        return 'false'

    
print(pal(-121))
