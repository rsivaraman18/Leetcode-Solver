####
# Example 1:
# from collections import Counter
# sentence = "Time waits for None"
# result = Counter(sentence)
# print("Result:",result)
# print("e-times: ",result['e'])

### Example 2 : With Dictionary
# import random
# obj_list = ['siva','python','developer']
# d = {}

# for i in range(50):
#     ran_val = random.choice(obj_list)
#     d[ran_val] = d.get(ran_val,0) +1
# print(d)
# O/P: {'programmer': 10, 'python': 8, 'siva': 15, 'developer': 17} 

### Example 3 : Using Counter

# import random
# from collections import Counter
# obj_list = ['siva','python','programmer','developer']
# count_box = Counter()

# for i in range(50):
#     ran_val = random.choice(obj_list)
#     count_box[ran_val] = count_box[ran_val]  +1
# print(count_box)

### Example 4 : Counter
# from collections import Counter
# obj_list = ['siva','python','develope','developer','developer','siva','python','siva','python',]
# counter = Counter(obj_list)
# print('counter',counter)