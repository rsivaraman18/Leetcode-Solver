 ''' 2108. Find First Palindromic String in the Array '''

def palindrome(words):
    for each in words:
        rev_word = each[::-1]
        if each == rev_word:
            print(each)
            return(each)
    else:
        print('***')
        return ''



palindrome(words = ["abc","car","ada","racecar","cool"])
palindrome(words = ["def","ghi"])
