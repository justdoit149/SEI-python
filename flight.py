from datetime import datetime, timedelta

num1 = input().split()
num2 = input().split()
begin1 = datetime.strptime(num1[0], "%H:%M:%S")  #调用datetime的函数对时间进行处理
end1 = datetime.strptime(num1[1], "%H:%M:%S")    #当你觉得某个功能可能有相应的python库函数时，一般都有
begin2 = datetime.strptime(num2[0], "%H:%M:%S")  #所以多尝试用现有的东西，不要反复造轮子
end2 = datetime.strptime(num2[1], "%H:%M:%S")    #当然，也不能不知道轮子怎么造

len_of_1 = len(num1)
len_of_2 = len(num2)
if len_of_1 == 3:
    if num1[2] == "(+1)":
        end1 += timedelta(days=1)
    elif num1[2] == "(+2)":
        end1 += timedelta(days=2)
if len_of_2 == 3:
    if num2[2] == "(+1)":
        end2 += timedelta(days=1)
    elif num2[2] == "(+2)":
        end2 += timedelta(days=2)

time = ((end2 - begin2) + (end1 - begin1)) / 2
hour,left = divmod(time.seconds, 3600)
minute,second = divmod(left, 60)
print(f"{hour:02}:{minute:02}:{second:02}")      #格式化输入输出的处理

