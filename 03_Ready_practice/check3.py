# import check2
# print("check3 ")
# print(check2.callme())
# print(check2.Greet)

# print('Check3:',__name__)

###### 
numbers = [1,2,11,22]

def square(x):
    if x >10:
        return x**2
    else:
        return x**3
    
greater = list( map(square, numbers))
big     = list(filter(square , numbers))

print('greater',greater)
print('big',big)