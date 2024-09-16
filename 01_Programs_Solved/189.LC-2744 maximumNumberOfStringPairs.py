
def maximumNumberOfStringPairs(words):
    count = 0
    for i,word in enumerate(words):
        sublist = words[:i] + words[i+1:]
        reverse = word[::-1]
        if reverse in sublist:
            print('Reverse {} and sublist {}'.format(reverse,sublist))
            count +=1
    print('Count:',count)
    result = int(count/2)
    return result



# maximumNumberOfStringPairs(words = ["cd","ac","dc","ca","zz"]) #2
# maximumNumberOfStringPairs(["ab","ba","cc"]) #1
maximumNumberOfStringPairs(words = ["aa","ab"]) #0

