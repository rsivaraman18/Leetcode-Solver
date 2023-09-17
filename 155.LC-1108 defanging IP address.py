''' 1108. Defanging an IP Address'''

def defanging(address):
    new = ''
    for char in address:
        if char =='.':
            new = new + '[.]'
        else:
            new = new + char
    print(new)
            


defanging("1.1.1.1" ) #"1[.]1[.]1[.]1"
defanging( "255.100.50.0")
