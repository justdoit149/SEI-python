def formatting(s,k): 
    s = "".join(s.split("-"))  #把原来的分隔符去掉
    LEN = len(s)
    divide_index = []          #存放分割点下标
    new_list = []
    divide_index.append(0)
    first_index = LEN % k
    if first_index == 0:
        first_index = k
    for i in range(1, (LEN - 1) // k + 2):
        divide_index.append(first_index)
        first_index = first_index + k
    LEN2 = len(divide_index)
    for i in range(LEN2-1):    #按照分割点来截取片段，放到一个新的列表里，最后把列表用"-"来分割。
        l = divide_index[i]
        r = divide_index[i+1]
        new_list.append(s[l:r].upper())
    return "-".join(new_list)


