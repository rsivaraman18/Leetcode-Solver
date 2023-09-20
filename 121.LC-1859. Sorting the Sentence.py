''' 1859. Sorting the Sentence '''

def sortsentence(s):
    d = { }
    out = ''
    
    s1 = s.split()
    for word in s1:
        new =int(word[-1]) 
        d[new] = word[:-1]
        
    for i in range(1,len(d)+1):
        if i ==1:
            out = out + d[i]
        else:
            out = out + ' ' +d[i]
    print(out)




def sortsentence1(s):
    d = { }
    out = ''
    
    s1 = s.split()
    for word in s1:
        new =int(word[-1]) 
        d[new] = word[:-1]
        
    for i in range(1,len(d)+1):
        out = out + d[i]
    print(out)


sortsentence("is2 sentence4 This1 a3")
sortsentence( "Myself2 Me1 I4 and3" )



















'''
Q1
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

'''

'''
Q2
Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
'''
