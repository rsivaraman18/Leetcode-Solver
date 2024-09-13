"""2703. Return Length of Arguments Passed"""

def program(s):
    max = len(s)
    count = 0
    for i in range(max):       
        if ((i+1) !=max):
            if s[i].lower() != s[i+1].lower():
                count +=1
    print('Count:',count)
    return count

program(s = "aAbBcC")
program( s = "AaAaAaaA")



 
