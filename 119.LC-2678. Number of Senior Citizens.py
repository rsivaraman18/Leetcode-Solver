'''2678. Number of Senior Citizens'''

'''
The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
'''

'''
Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
Output: 2
Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
'''

'''
Input: details = ["1313579440F2036","2921522980M5644"]
Output: 0
Explanation: None of the passengers are older than 60.
'''

def senior(s):
    senior = [ ]
    for i in s:
        new = int(i[11:13])
        if new>60:
            senior.append(new)
            print(senior)

    print(len(senior))


senior(["7868190130M7522","5303914400F9211","9273338290F4010"])
senior(["1313579440F2036","2921522980M5644"])











