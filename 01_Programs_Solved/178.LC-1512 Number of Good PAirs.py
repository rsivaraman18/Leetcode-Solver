
"""  1512 Number Of Good Pairs """

def program(nums):
    max_length = len(nums)
    result=[]
    for i in range(max_length):
        for j in range(0,max_length):
            if (i!=j) and (nums[i] == nums[j]):
                result.append([i,j])

    count = len(result)//2
    print('Result:',result)
    print('Count:',count)
    return count

            
program(nums = [1,2,3,1,1,3])
program(nums =[1,1,1,1])
program(nums = [1,2,3])


