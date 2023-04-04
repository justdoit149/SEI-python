# num = float(input('请输入一个数字： '))
# num_sqrt = num ** 0.5          #对正数，开平方可以用0.5次方来计算
# print('%0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

 
# 计算实数和复数平方根
# 导入复数数学模块
import cmath    #math是普通实数数学库，cmath是复数数学库
 
num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# In：请输入一个数字: -8
# Out：-8 的平方根为 0.000+2.828j