''' 2278 percentage-of-letter-in-string '''
def percentage(s,letter):
    import math
    lcount = s.count(letter)
    print(lcount)
    print( len(s))
    per = lcount/ len(s)
    per = per * 100
    per = math.floor(per)
    print (per)
    print('****************')


    


percentage(s = "foobar", letter = "o")
percentage(s = "jjjj", letter = "k" )
percentage("sgawtb" ,"s")




'''
Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
'''

'''
Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
'''
