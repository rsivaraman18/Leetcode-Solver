'''  1876. Substrings of Size Three with Distinct Characters  '''

def substring(s):
    mylist = [ ]
    for i in range(0,len(s)):
        if len(s)>=i+3:
            word = s[i:i+3]
            
            mylist.append(word)
    print(mylist)
    result = [ ]
    for each in mylist:
        if  ( each[0]==each[1] or each[0]==each[2] or each[1]==each[2] ):
            pass
        else:
            result.append(each)
    print(len(result))
            

'''
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
'''

'''
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
'''

        
        
        
            
    
            
                




substring( "xyzzaz")
substring( "aababcabc")
