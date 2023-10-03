''' 657. Robot Return to Origin '''
def judgeCircle(moves):
    d = {'D':0,'U':0,'L':0,'R':0}
    
    for i in moves:
        d[i] = d.get(i,0) + 1
        #print(d)
        
    if d['U'] == d['D'] and d['L'] == d['R']:
        print('true')
        return True
    else:
        print('false')
        return False
        
    



    
judgeCircle("UD")    
judgeCircle("LL") 
