''' 383. Ransom Note '''
def ransomenote(ransomNote,magazine):
    dran = {}
    dmag = {}
    for letter in ransomNote:
        dran[letter] = dran.get(letter,0) + 1
    for letter in magazine:
        dmag[letter] = dmag.get(letter,0) + 1

    for key in dran.keys():
        try:
            if dran[key] > dmag[key] :
                return False
        except KeyError:
            return False
    return True



ransomenote(ransomNote = "a", magazine = "b") # false
ransomenote(ransomNote = "aa", magazine = "ab") # false
ransomenote(ransomNote = "a", magazine = "aab") # true
ransomenote(ransomNote = "aab", magazine = "baa" ) #true


print('********************************************')

def ransomenote2(ransomNote, magazine):
    from collections import Counter
    ransom = Counter(ransomNote)
    mag = Counter(magazine)
    
    # Check if the common elements cover the entire ransom note
    if all(ransom[char] <= mag[char] for char in ransom):
        print('true')
    else:
        print('false')
    



ransomenote2(ransomNote = "a", magazine = "b") # false
ransomenote2(ransomNote = "aa", magazine = "ab") # false
ransomenote2(ransomNote = "a", magazine = "aab") # true
ransomenote2(ransomNote = "aab", magazine = "baa" ) #true

print('********************************')




def ransomenote3(ransomNote,magazine):
    from collections import Counter
    ransome = Counter(ransomNote)
    mag = Counter(magazine)
    if ransome & mag == ransome:
        print('true')
    else:
        print('false')



ransomenote3(ransomNote = "a", magazine = "b") # false
ransomenote3(ransomNote = "aa", magazine = "ab") # false
ransomenote3(ransomNote = "a", magazine = "aab") # true
ransomenote3(ransomNote = "aab", magazine = "baa" ) #true