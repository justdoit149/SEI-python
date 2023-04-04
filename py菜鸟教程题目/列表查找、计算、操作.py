list1 = [12, 0.4, 43, -3,0, -9.9, 12, 1, 12, -3]

print(43 in list1)             #查找是否存在，返回True/False       
print(list1.index(43))         #查找下标，找不到则ValueError，可以try……exceept判断，或结合 in
print(list1.count(12))         #计数出现次数
print(sum(list1))              #求和
print(max(list1),min(list1))   #求最值

list1.clear()                  #清空列表
print('清空后:', list1)
