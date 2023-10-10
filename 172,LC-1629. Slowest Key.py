''' 1629. Slowest Key '''
def slowestKey(releaseTimes,keysPressed):
    d = {}
    for i in range (len(keysPressed)):
        if i == 0:
            val = releaseTimes[i] - 0
        else:
            val = releaseTimes[i] - releaseTimes[i-1]
        d[i] = val
    
    max_value = max(d.values())
    

    keys_with_max = [ ]
    for key, value in d.items():
        if value == max_value:
            keys_with_max.append(keysPressed[key])


    # Lexicography Sort 
    result = sorted(keys_with_max)
    print(result[-1])
    return result[-1]



slowestKey([9,29,49,50] ,  "cbcd" )