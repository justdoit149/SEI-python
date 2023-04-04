def to_do(list1):
    LEN = len(list1)
    for i in range(LEN):
        find = False
        for j in range(LEN):
            if list1[i] == list1[j] and i != j:
                find = True
        if find == True:
            continue
        else:
            return list1[i]
    
list1 = list(input().split())
print(to_do(list1))