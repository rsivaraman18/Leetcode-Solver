''' 1694. Reformat Phone Number '''

def phone(number):
    newphone = ''
    for i in number:
        if i.isdigit():
            newphone =newphone+i
    print(newphone)
    while True:
        new = newphone[0:4]
        print(new)
            
    print(newphone)



phone(number = "1-23-45 6")
