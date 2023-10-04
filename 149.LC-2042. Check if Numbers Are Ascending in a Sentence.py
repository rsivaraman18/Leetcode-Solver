'''  2042. Check if Numbers Are Ascending in a Sentence   '''


def incnum(s):
    numbers = [ ]
    word = s.split()
    for each in word:
        if each.isnumeric():
            numbers.append(int(each))
    print(numbers)

    flag = 'True'
    old = 0
    for num in numbers:
        new = num
        if num > old:
            old = new
            flag='True'
        else:
            return False
            
            
    print(flag)
          

#incnum(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles")
#incnum(s ="hello world 5 x 5")
incnum("hello world 5 x 5")
