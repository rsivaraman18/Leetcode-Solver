  # 175.LC-58. Length of the Last Word.py
  
     
 
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

 


def program(s):
    new_list= s.split(' ')
    result = []
    for each in new_list:
        if each !="":
            result.append(each)
    lastword = result[-1]
    length = len(lastword)       
    print("Last word is '{}' and length is '{}'".format(lastword,length))

program("Hello World")
program("   fly me   to   the moon  ")
program("luffy is still joyboy")
