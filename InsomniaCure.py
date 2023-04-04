k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input()) 
a = [1]   #先把a[0]填上，后续从1开始更方便。也可以a = []，这样后面就是从0开始了
for i in range(d):
    a.append(1)   #在列表a后面添加元素
for i in range(1,d+1):  #从1到d+1（左闭右开）
    if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
        a[i] = 0
print(a.count(0))  #依旧是用好现成的轮子

