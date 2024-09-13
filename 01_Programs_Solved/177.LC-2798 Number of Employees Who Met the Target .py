"""2798. Number of Employees Who Met the Target"""
"""EXAMPLE 1
    Input: hours = [0,1,2,3,4], target = 2
    Output: 3
    Explanation: The company wants each employee to work for at least 2 hours.
    - Employee 0 worked for 0 hours and didn't meet the target.
    - Employee 1 worked for 1 hours and didn't meet the target.
    - Employee 2 worked for 2 hours and met the target.
    - Employee 3 worked for 3 hours and met the target.
    - Employee 4 worked for 4 hours and met the target.
    There are 3 employees who met the target.
"""
"""EXAMPLE 2
    Input: hours = [5,1,4,2,2], target = 6
    Output: 0
    Explanation: The company wants each employee to work for at least 6 hours.
    There are 0 employees who met the target.
"""



def numberOfEmployeesWhoMetTarget(hours,target):
    sum = 0
    for hour in hours:

        if hour>=target:
            sum += 1
    print('Final Output :',sum)
    return sum

numberOfEmployeesWhoMetTarget( [0,1,2,3,4],target=2)
numberOfEmployeesWhoMetTarget( [5,1,4,2,2],target=6)

numberOfEmployeesWhoMetTarget([0,1,2,3,4],target=2)
