
### LC-3042 countPrefixSuffixPairs 
### But One Test Case Error Occurs
def countPrefixSuffixPairs(words):
    count = 0 
    for i, word in enumerate(words):
        sublist = words[:i] + words[i+1:]
        for each in sublist:
            length = len(word)
            fword = each[:length]
            lword = each[-(length):]
            if (word == fword) and (word ==lword):
                count +=1
    print('Count:',count)
    
            
    
countPrefixSuffixPairs(words = ["a","aba","ababa","aa"])  ## Output 4
countPrefixSuffixPairs(words = ["pa","papa","ma","mama"])  ## Output 2
countPrefixSuffixPairs(words = ["abab","ab"])                 ## Output 0


