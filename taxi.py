n = int(input())    #input默认字符串格式，需要自己转换成整数
s = list(map(int,input().split()))  
#input().split()用空格分开，map把分开的每一节转化为int，list把整一串转换成列表
s1 = s.count(1)  #变量.函数()，用来处理变量，s.count(x)即计数列表s里x的出现次数
s2 = s.count(2)
s3 = s.count(3)
s4 = s.count(4)
# for i in range(n):    #自己造轮子的写法
#     if s[i] == 1:
#         s1 = s1 + 1
#     elif s[i] == 2:
#         s2 = s2 + 1
#     elif s[i] == 3:
#         s3 = s3 + 1
#     elif s[i] == 4:
#         s4 = s4 + 1
#     else:
#         pass
if(s1 <= s3):
    out = s4 + s3 + (s2 + 1) // 2 
else:
    out = s4 + s3 + (s1 - s3 + 2 * s2 + 3) // 4
# 其实可以整合成out = s4 + s3 + (max(s1 - s3, 0) + 2 * s2 + 3) // 4
print(out)
