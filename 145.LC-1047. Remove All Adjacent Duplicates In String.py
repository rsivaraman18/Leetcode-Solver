def adremove(s):
    mylist = ['']
    print('Given',s) 
    for i in range (0,len(s)):
        new = (len(mylist)-1)
        
        if s[i]!= mylist[new]:
            mylist.append(s[i])
            
        elif s[i]== mylist[new]:
            mylist.pop(new)
        else:
            print('Err')

    
    mylist.remove('')
    result = ''.join(mylist)
    print(result)
            
    
adremove( "abbaca")
adremove("azxxzy")
adremove("aababaab") #babb
