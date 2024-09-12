''' 1957. Delete Characters to Make Fancy String '''

def fancy(s):
    ans, last, count = [], "", 0
    for ch in s:
        if ch == last:
            count += 1
        else:
            count = 0
        if count < 2:
            ans.append(ch)
        last = ch
    print( "".join(ans) )
    
fancy(s = "leeetcode")
fancy(s = "aaabaaaa")
fancy(s = "aab")
