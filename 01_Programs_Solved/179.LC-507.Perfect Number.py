"""  3146.permutation difference"""

179.LC-507.Perfect Number.py
def permutation(s,t):
    total = 0
    for letter in s:
        sindex = s.find(letter)
        tindex = t.find(letter)
        diff = abs(sindex-tindex)
        total += diff
    print('Total:',total)
    return total


permutation( s = "abc", t = "bac")
permutation(s = "abcde", t = "edbac")
