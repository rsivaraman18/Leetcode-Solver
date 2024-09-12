''' 1678. Goal Parser Interpretation '''

def goal(command):
    out=''
    i=0
    while (i<len(command)):
        print('Check',command[i],'index',i)
    
        if command[i]=='G':
            out = out + 'G'
            i = i+1
            
        elif command[i]=='(':
            if command[i+1]==')':
                out = out + 'o'
                i = i+2
            else:
                out = out + 'al'
                i = i+4
        else:
            print('Eroor')
            i =i+1
                
    print('Result',out)
    print('***')
            
#goal( "G()(al)" )
goal('G()()()()(al)')
goal( "(al)G(al)()()G")
            
