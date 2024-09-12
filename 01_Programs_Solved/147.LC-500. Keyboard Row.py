''' 500. Keyboard Row '''
def keyboard(words):
    #first  = ['q','w','e','r','t','y','u','i','o','p']
    f = 'qwertyuiop'
    s = 'asdfghjkl'
    t = 'zxcvbnm'
    final = []
    for word in words:
        org    = word
        word   = word.lower()
        lword  = len(word)
        fcount = scount= tcount =0
        
        for letter in word:    
            if letter in f:
                fcount = fcount + 1
            elif letter in s:
                scount = scount + 1
            elif letter in t:
                tcount = tcount + 1
                
        if (fcount==len(word)) or (scount==len(word)) or (tcount==len(word)) :
            final.append(org)
                
    print(final)

            
    
keyboard(["Hello","Alaska","Dad","Peace"])
        
             
'''

keyboard( ["Hello","Alaska","Dad","Peace"])
keyboard( ["omk"] )
keyboard( words = ["adsdf","sfd"])
'''
