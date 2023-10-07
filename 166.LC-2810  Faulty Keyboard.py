''' 2810. Faulty Keyboard  '''
#   Input = "string"  --> Output = 'rtsng'
#   Input = "poiinter" --> Output =  "ponter"


def Keyboard(s):
    result = ''
    for letter in s:
        if letter !='i':
            result += letter
        else:
            result = result[::-1]
    return result
    
        




Keyboard('string')

Keyboard('poiinter')
