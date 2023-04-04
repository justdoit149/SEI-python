import csv
def getcommand(file):
    n = int(input())
    for i in range(n):
        line = input()
        if line[0:6] == "INSERT":
            f = open(file, "a+")     #a表示追加模式，+表示可读可写
            end = len(line)
            line2 = line[7:end]      #截取 
            f.write("\n"+line2)      #在文件末尾写入
            f.close()                #及时关闭打开的文件
        elif line[0:7] == "SHOWALL": 
            f = open(file,"r")       #只读模式打开
            countline = len(f.readlines())       #获取文件行数
            f.close()
            f = open(file,"r")                   #将标识符重新设置到开头位置
            filelist = []
            for i in range(countline):
                filelist.append(f.readline().split(','))   #将字符串分割为列表之后存入大列表中
            filelist = sorted(filelist, key = lambda x:float(x[2])) #lambda表达式按照第2列排序
            wide1,wide2,sum = 4,5,0           #注意上面第二列原本是字符串，必须转换为浮点数再排序
            for i in range(countline):        #这个循环用来获取输出列宽度和平均值
                len1, len2 = len(filelist[i][0]), len(filelist[i][1])
                if len1 > wide1:
                    wide1 = len1
                if len2 > wide2:
                    wide2 = len2
                sum = sum + float(filelist[i][2])
            wide1, wide2 = wide1+1, wide2+1
            print("{0:<{wide}}".format('Name',wide = wide1),end = '')
            print("{0:<{wide}}".format('Title',wide = wide2),end = '')
            print('Salary')
            for i in range(countline):
                print("{0:<{wide}}".format(filelist[i][0],wide = wide1),end = '')
                print("{0:<{wide}}".format(filelist[i][1],wide = wide2),end = '')
                print("{0:.2f}".format(float(filelist[i][2])))
            print("AVG:{0:.2f}".format(sum/countline))
            f.close()
