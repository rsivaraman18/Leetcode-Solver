### Error Occurs at Test case600

def min_distance_circular_list(words, startIndex, target):
    n = len(words)
    
    # Find the index of the target letter
    if target not in words:
        return -1  # target not found in list
    
    target_idx = words.index(target)
    print(target_idx)
    
    # Calculate clockwise distance
    if target_idx >= startIndex:
        clockwise_distance = target_idx - startIndex
    else:
        clockwise_distance = n - startIndex + target_idx
    print('Clockwise value:',clockwise_distance)
    # Calculate counter-clockwise distance
    if startIndex >= target_idx:
        counter_clockwise_distance = startIndex - target_idx
    else:
        counter_clockwise_distance = startIndex + (n - target_idx)
    print('AntiClockwise value:',counter_clockwise_distance)
    # # Return the minimum of the two distances

    result =  min(clockwise_distance, counter_clockwise_distance)
    return result


# min_distance_circular_list(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1)  # Output should be 2
# min_distance_circular_list( words = ["a","b","leetcode"], target = "leetcode", startIndex = 0)
# print(min_distance_circular_list(words = ["i","eat","leetcode"], target = "ate", startIndex = 0))
print(min_distance_circular_list(words =
["odjrjznxpn","cyulttuabe","zqxkdoeszk","yeewpgriok","odjrjznxpn","btqpvxpjzv","ukyudladhk","ukyudladhk","odjrjznxpn","yeewpgriok"],target="odjrjznxpn",startIndex =
5))