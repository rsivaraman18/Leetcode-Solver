# 176.LC-507.Perfect Number.py
     
# def program(num):
#     result = []
#     for i in range(1,num):
#         if num%i==0:
#             result.append(i)
#     tot  = sum(result)
#     if tot == num:
#         print('True')
#         return True
#     else:
#         print('False')
#         return False

 
# program(28)
# program(7)



def program(num):
    total = 0
    for i in range(1,num):
        if num%i==0:
            total += i
    if total == num:
        print('True')
        return True
    else:
        print('False')
        return False


program(28)
program(7)
