'''944. Delete Columns to Make Sorted'''

def sort_columns(strs):
    d = {}
    for i in range(len(strs)):
        for j in range(len(strs[0])):
            new = strs[i][j]
            d[j] = d.get(j,'') + new

    count = 0
    for value in d.values():
        svalue = ''.join(sorted(value))
        if svalue != value:
            count = count +1
    print('No of columns not sorted is: ',count)



sort_columns(strs = ["zyx","wvu","tsr"])
sort_columns(strs = ["cba","daf","ghi"])
sort_columns(strs = ["a","b"])
