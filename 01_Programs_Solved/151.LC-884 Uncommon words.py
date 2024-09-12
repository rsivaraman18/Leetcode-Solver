''' 884. Uncommon Words from Two Sentences '''
def Uncommon(s1,s2):
    uncommon = []
    s1 = s1.split()
    s2 = s2.split()
    
    for word in s1:
        wcount = s1.count(word) # only once in sentence
        if word not in s2 and wcount==1:
            uncommon.append(word)

    for word in s2:
        wcount = s2.count(word) # only once in sentence
        if word not in s1 and wcount==1:
            uncommon.append(word)
        
            
    print(uncommon)


Uncommon(s1 = "this apple is sweet", s2 = "this apple is sour")
Uncommon(s1 = "apple apple", s2 = "banana")   
