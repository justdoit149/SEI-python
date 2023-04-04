#Python的数组本身就是动态可变的，同时提供append（）函数，该函数可以在一个数组后面添加数字、数组
x, y = 0, 0                     #常量可以放在一起赋值
last = ' '
error = 0
qipan = [[] for i in range(10)] #二维数组的生成（重要），多种方法
for i in range(10):
    for j in range(10):
        qipan[i].append(' ')#.append()表示添加，二维数组实际上是一维数组的每个位置可以是一个元素也可以是数组
                            #而如果不加.append则视作把这个位置当做一个元素
n = int(input())            #input默认以字符串存储，int、float等转化python自己帮你实现，不需要你考虑ascii计算

for i in range(n):          #循环里，range(begin,end,pace)三个参数，end必须有，begin默认0，pace默认1,算头不算尾
    act = input().split()   #把一行里的输出用空格分开，以列表的形式存储到act里
    len_of_act = len(act)   #len函数获取列表的长度，便于分类讨论
    if(len_of_act == 3):
        last = act[2]
    if act[0] == 'R':
        if y + int(act[1]) > 9 or y + int(act[1]) < 0:#py里位运算和c一样，但是and和or就是直接用英文单词
            print("Error!")
            error = 1       #oj上好像不能用exit()来退出，应该是因为oj上exit会直接把测试之类的也停掉？                         
            break           #所以就用最原始的方法吧
        for j in range(int(act[1])):
            y = y + 1
            qipan[x][y] = last
    elif act[0] == 'L':
        if y - int(act[1]) > 9 or y - int(act[1]) < 0:
            print("Error!")
            error = 1
            break
        for j in range(int(act[1])):
            y = y - 1
            qipan[x][y] = last
    elif act[0] == 'U':
        if x - int(act[1]) > 9 or x - int(act[1]) < 0:
            print("Error!")
            error = 1
            break
        for j in range(int(act[1])):
            x = x - 1
            qipan[x][y] = last
    elif act[0] == 'D':
        if x + int(act[1]) > 9 or x + int(act[1]) < 0:
            print("Error!")
            error = 1
            break
        for j in range(int(act[1])):
            x = x + 1
            qipan[x][y] = last  

if error == 0:
    for i in range(10):
        for j in range(10):              #print末尾默认换行，可以用end = '……'来改变末尾字符
            print(qipan[i][j],end = '')  #不能直接print(qipan[i]),那样输出一整个列表，包括中括号之类的东西
        print()                          #用来换行
    