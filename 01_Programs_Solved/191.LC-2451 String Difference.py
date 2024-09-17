### 2451 String Difference



def oddString(words):
    ## To find the Logic Distance between String
    values = []
    text = 'abcdefghijklmnopqrstuvwxyz'
    for i, word in enumerate(words):
        max_length = len(word)
        ind_word = []
        for i in range(max_length-1):
            a = text.find(word[i])
            b = text.find(word[i+1])
            diff = b-a
            ind_word.append(diff)
            
        values.append(ind_word)
    print(values)

    ### To Find Unique Among a List of Values:
    unique = ''
    for i in range(len(values)):
        sublist = values[:i] + values[i+1:]
        if values[i] not in sublist:
            unique = words[i]
        
    print('Unique',unique)

    

# Example usage
oddString(words = ["adc", "wzy", "abc"])   ###output 

oddString(words =["mll","edd","jii","tss","fee","dcc","nmm","abb","utt","zyy","xww","tss","wvv","xww","utt"])
oddString(["nnnmmmnnmmmmmmmmmmnm","iiihhhiihhhhhhhhhhih","aaaabbbbbbaaabaaaabb","qqqpppqqppppppppppqp","eeedddeedddddddddded","eeedddeedddddddddded","iiihhhiihhhhhhhhhhih","lllkkkllkkkkkkkkkklk","sssrrrssrrrrrrrrrrsr","sssrrrssrrrrrrrrrrsr","jjjiiijjiiiiiiiiiiji","nnnmmmnnmmmmmmmmmmnm","xxxwwwxxwwwwwwwwwwxw","eeedddeedddddddddded","zzzyyyzzyyyyyyyyyyzy","wwwvvvwwvvvvvvvvvvwv","cccbbbccbbbbbbbbbbcb","xxxwwwxxwwwwwwwwwwxw","cccbbbccbbbbbbbbbbcb","yyyxxxyyxxxxxxxxxxyx","hhhggghhgggggggggghg"])



"""
Example 1:

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation: 
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, "abc".
Example 2:

Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].
 

"""









