"""write your code in following methods"""
file_path = './tasks.txt'

#这个函数用来把输入行的参数项分离成列表并返回
#其参数line为去头后的输入行，LEN为line的长度
def MySplit(line,LEN):
    count = 0
    list = []
    list_index = [-1]          #首尾分别是-1和LEN
    for i in range(LEN):
        if line[i] == '"':
            count += 1
        elif line[i] == ' ':   #不在引号里的空格作为分隔符，记录下标
            if count % 2 == 0:
                list_index.append(i)
    list_index.append(LEN)
    LENLIST = len(list_index)
    for i in range(1,LENLIST): #最后按照下标来截取片段并形成参数列表
        list.append(line[list_index[i-1]+2:list_index[i]-1])
    return list


#这个函数寻找并返回要删除、修改的行的行数，按照行数从小到大排好序返回
#其参数CopyFile为文件的拷贝，list为要找的参数列表，LENLIST为参数列表长度
#注意CopyFile = f.readlines(),其是一个列表，列表长度是行数，每一行放在列表的一个位置中(保留回车符)
def FindIndex(CopyFile,list,LENLIST):
    IndexList = []
    LENTXT = len(CopyFile)
    for i in range(LENLIST):
        for j in range(LENTXT):
            if "todo:"+list[i]+"\n" == CopyFile[j]:#比较，一致则将下标添加到新列表中
                IndexList.append(j)
                break
    IndexList.sort() #把新列表中的下标值从小到大排好序
    return IndexList


def to_do():
    while True:
        line = input()
        if line:      #如果不是空行就循环，是空行则break。
            LEN = len(line)
            CASE = line[5:8]
            line = line[8:LEN]
            LEN -= 8
            list = MySplit(line,LEN)
            LENLIST = len(list)
            if CASE == "-a ":
                f = open(file_path,'a+')     #a+:可读可写，追加模式
                for i in range(LENLIST):
                    f.write("todo:"+list[i]+"\n")
                f.close()
            elif CASE == "-d " or CASE == "-c ": #这两个处理方式类似，放在一起
                f = open(file_path,'r+')     #r+:可读可写，指向开头
                CopyFile = f.readlines()     #用这个拷贝、暂存文件，便于修改           
                f.close()
                IndexList = FindIndex(CopyFile,list,LENLIST)  #找到要删除/修改的位置
                LEN_IndexList = len(IndexList)
                for i in range(LEN_IndexList-1,-1,-1):  #删除:从后到前处理
                    if CASE == "-d ":
                        del CopyFile[IndexList[i]]
                    else:
                        temp = CopyFile[IndexList[i]]   #修改:截取后半部分，把completed与之拼接
                        CopyFile[IndexList[i]] = "completed"+temp[4:len(temp)]
                f = open(file_path,"w+")     #w+:可读可写，打开时清空文件。
                f.write(''.join(CopyFile))   #修改之后再写回。注意转换成字符串(已经含回车，所以无分隔)
                f.close()
            elif CASE == "-f " or CASE == "-al":
                f = open(file_path,'r')      #只读，不可写入/修改。指向开头
                CopyFile = f.readlines()
                LENFILE = len(CopyFile)
                f.close()
                if CASE == "-al":              #全部输出  
                    for i in range(LENFILE):
                        print(CopyFile[i],end='')
                elif line == "todo":           #只输出todo行
                    for i in range(LENFILE):
                        if CopyFile[i][0:4] == "todo":
                            print(CopyFile[i],end='')
                elif line == "completed":      #只输出completed行
                    for i in range(LENFILE):
                        if CopyFile[i][0:9] == "completed":
                            print(CopyFile[i],end='')     
            elif CASE == "-qu":                #直接break跳出大循环，最终return
                break
            else:
                pass
        else:
            break
    return
