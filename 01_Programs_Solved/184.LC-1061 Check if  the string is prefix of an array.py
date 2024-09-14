

"""1961 Check if the string is prefix of an array"""
def isPrefixString(s,words):
    slen = len(s)
    result=''
    flag = False
    for word in words:
        result +=word 
        if result == s:
            flag = True
            break
    print('Flag',flag)
    return flag
        

        


isPrefixString( s = "iloveleetcode", words = ["i","love","leetcode","apples"])
isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"])
