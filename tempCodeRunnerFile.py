def isPetyaLanguage():
    sentence = input().split()
    LEN = len(sentence)
    index = -1    #标记遇到的第一个名词的下标
    gender = -1   #标记性别，male为0，female为1
    for i in range(LEN):
        if sentence[i].endswith('etr'):
            gender = 0
            index = i
            break
        elif sentence[i].endswith('etra'):
            gender = 1
            index = i
            break
    if index == -1:
        print("NO")
    else:
        if gender == 0:
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
