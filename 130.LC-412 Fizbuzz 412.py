#  ( )
''' 412: Time 97.26%, Solution with step by step explanation '''

def fizzbuzz(n):
    out = []
    for i in range(1,n+1):
        if (i%3==0) and (i%5==0):
            out.append('FizzBuzz')
        elif (i%3==0):
            out.append('Fizz')
        elif (i%5==0):
            out.append('Buzz')
        else:
            out.append(str(i))
    print(out)
    print('********************')
            
            
    




fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)

'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''


