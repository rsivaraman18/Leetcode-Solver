def check(items,ruleKey,ruleValue):
    litem = len(items) 
    d = {'type':0 , 'color':1 , 'name':2}
    count = 0
    
    for i in range(litem):
        j = d[ruleKey]
        if items[i][j] ==ruleValue:
            count += 1
    print('count',count)



check(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
      ruleKey = "color", ruleValue = "silver")
check(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
      ruleKey = "type", ruleValue = "phone")
