'''
Input: s = "RLRRLLRLRL"
Output: 4
"RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
'''


def balanced(s):
    
    d = {"R":0,"L":0}
    out =''
    li = []
    
    for i in s:       
        if i == 'R':
            d['R'] = d['R'] + 1
            out = out + 'R'      
            
        else:  
            d['L'] = d['L'] + 1
            out = out + 'L'

        if (d['R'] == d['L'] ):
            li.append(out)
            out = ''
            
        
    print(li)
    print(len( li))
    
          
balanced("RLRRLLRLRL")
balanced("RLRRRLLRLL") 
balanced("LLLLRRRR")

