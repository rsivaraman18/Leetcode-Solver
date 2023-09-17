''' 1816. Truncate Sentence  '''

def truncate(s,k):
    sent = s.split()
    print(sent)
    
    result = [ ]
    for i in range(0,k):
        result.append(sent[i])
    print(result)
 
    
    out = ' '.join(result)
    print(out)
    print('********')
    


truncate( "Hello how are you Contestant", k = 4)
    
truncate(  "What is the solution to this problem", k = 4 )
truncate(  s = "chopper is not a tanuki", k = 5 )
