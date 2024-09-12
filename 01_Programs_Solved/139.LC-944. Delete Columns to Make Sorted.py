''' 944. Delete Columns to Make Sorted  '''

def deletecol(strs):
    new = [ ]
    count = 0
    for i in range(len(strs)):
        out = ''
        for j in range(len(i)):
            out = out + strs[j][i]
        new.append(out)

    print(new)

    for each in new:
        old = each
        new = sorted(each)
        new = ''.join(new)
        if old != new:
            count = count +1
    
    print(count)
    print('**********')
        






#deletecol(["abc", "bce", "cae"])
 
deletecol( ["cba","daf","ghi"] )
#deletecol( ["a","b"] )
#deletecol(["zyx","wvu","tsr"])


'''
strs = ['a','b']
for i in range(1):
    out = ''
    for j in range(1):
        out = out + strs[j][i]
        print(out)

'''







    




