
# error pops
def title(word):
    word = title
    new = word.split( )
    out = ''

    for i in new:
        if len(i)>2:
            if new[0] == i:
                out = out + i.title( )
            else:
                    out = out + ' ' + i.title( )
        else:
            if new[0] == i:
                out = out + i.lower( )
            else:
                out = out + ' ' + i.lower( )

                
            
        return out
title( "capiTalIze tHe titLe")


'''
name ='rivaraman'
out = name.title( )
print(out)
'''
