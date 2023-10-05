''' 156.LC-2011 Final Value of Variable After Performing Operations '''

def finvalue(operation):
    add = ["++X" , "X++"]
    sub = ["--X" , "X--"]
    count = 0
    for each in operations:
        if each in add:
            count +=1
        elif each in sub:
            count -=1   
        else:
            print('Error')
    print(count)


finvalue(["--X","X++","X++"])
finvalue(["++X","++X","X++"])

'''
count = 0
    for each in operation:
        print('each',each)
        if each == "++X" or "X++" :
            count = count +1
        else:
            count = count -1
    print('count',count)

'''
