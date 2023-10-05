''' 1189. Maximum Number of Balloons '''

def ballonnum(text):
    target = 'balloon'
    selected = []
    num_check = 0
    check =0
    out = ''
    
    for char in text:
        if char in target:
            selected.append(char)
            if char=='b':
                num_check = num_check+1
    print(selected)
    print(num_check)

    
    while(num_check>check):
        
        for char in target:
            if char in selected:
                selected.remove(char)
                out = out + char
            else:
                break
                print('bye')
        out = out + ' '
        check = check+1
    print(out)
    ballons = out.split()
    no_of_ballons = ballons.count(target)
    print(no_of_ballons)
                

#ballonnum( "nlaebolkonlaebolko")
#ballonnum("ballon")

def solution2(text):
    from collections import Counter
    import math
    
    s = Counter(text)
    print(s)
    ans = 0
    ans = min(s.get('b',0),s.get('a',0),s.get('n',0),math.floor(s.get('l',0)/2),math.floor(s.get('o',0)/2),)
    print(ans)


solution2("nlaebolkonlaebolko")

