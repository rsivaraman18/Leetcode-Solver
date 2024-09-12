''' 1945. Sum of Digits of String After Convert '''

def sumofdigit(s,k):
    d = {}
    alpha = '0abcdefghijklmnopqrstuvwxyz'
    for i in range(1,27):
        new = alpha[i]
        d[new] = i
    print(d)

    digit = ''
    for char in s:
        digit = digit + str(d[char])
    print(digit)

    i = 0
    while(k  > i):
        tot = 0
        for each in digit:
            tot = tot + int(each)
        
        digit = str(tot)
        i = i+1
    print(tot)        
        

def solution2(s,k):
    string = ""
    for char in s:
        num = ord(char) - 96
        string += str(num)

    res = 0
    while k > 0:
        res = 0
        for char in string:
            res += int(char)
            # print(string, res)
        string = str(res)
        k -= 1
    print( res)


#sumofdigit("zbax",2)
#sumofdigit( s = "leetcode", k = 2)

solution2("zbax",2)
