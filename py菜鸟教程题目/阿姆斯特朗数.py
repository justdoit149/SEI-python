# Python 检测用户输入的数字是否为阿姆斯特朗数
#如果一个 n 位正整数等于其各位数字的 n 次方之和，则称该数为阿姆斯特朗数。 例如 1^3 + 5^3 + 3^3 = 153。
num = int(input("请输入一个数字: "))
sum = 0
n = len(str(num))  #想要知道整数的位数，可以先转化为字符串再用len函数
 
# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")