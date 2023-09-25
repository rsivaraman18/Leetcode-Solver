''' 2506. Count Pairs Of Similar Strings '''

def Counting(words):
    arrange = [ ]
    count = 0
    for each in words:
        new = set( ) 
        for let in each:
            new.add(let)
        new = sorted(new)
        new = ''.join(new)
        
        arrange.append(new)

    for i in range(0,len(arrange)):
        for j in range(i+1,len(arrange)):
            if arrange[i] == arrange[j]:
                count = count + 1
    print(count)
                

Counting(["aba","aabb","abcd","bac","aabc"] )
Counting( ["aabb","ab","ba"] )
Counting(  ["nba","cba","dba"] )



'''
print(arrange)
    print(set(arrange))
    out = len(arrange) - len((set(arrange)))
    print(out)
    print('*****************************')
'''



'''
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.
'''
