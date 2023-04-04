def isPetyaLanguage():
    sentence = input().split()
    LEN = len(sentence)
    index = -1            #标记遇到的第一个名词的下标
    gender = -1           #标记性别，male为0，female为1
    if LEN == 1:          #处理单个词的情况
        if sentence[0].endswith('etr')\
        or sentence[0].endswith('etra')\
        or sentence[0].endswith('lios')\
        or sentence[0].endswith('initis')\
        or sentence[0].endswith('liala')\
        or sentence[0].endswith('inites'):
            print('YES')
        else:
            print('NO')
        return            #函数里return提前返回
    #处理整个句子的情况
    for i in range(LEN):  #找名词，标记核心词和属性
        if sentence[i].endswith('etr'):      #.endswith()函数，判断字符串末尾
            gender = 0
            index = i
            break
        elif sentence[i].endswith('etra'):
            gender = 1
            index = i
            break
    if index == -1:       #找不到名词 
        print("NO")
    else:
        if gender == 0:   #以index划分，前面后面分别判断
            for i in range(index):
                if sentence[i].endswith('lios'):
                    continue
                else:
                    print("NO")
                    return
            for i in range(index+1,LEN):
                if sentence[i].endswith('initis'):
                    continue
                else:
                    print("NO")
                    return
        elif gender == 1:
            for i in range(index):
                if sentence[i].endswith('liala'):
                    continue
                else:
                    print("NO")
                    return
            for i in range(index+1,LEN):
                if sentence[i].endswith('inites'):
                    continue
                else:
                    print("NO")
                    return
        print("YES")
    return