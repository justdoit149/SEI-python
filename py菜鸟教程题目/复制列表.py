# li1 = [4, 8, 2, 10, 15, 18]
# li2 = li1  #实际上这里li1、li2都像是一个指向一块空间的指针
# print(li1,li2)   
# li1[5] = 0    #这里修改列表是直接对这块空间操作，所以li1和li2都跟着改变
# print(li1,li2)
# li1 = [1,2,3]   #这里是原来那块空间没变，li1指向了新的一个列表对应的空间，所以li2不改变
# print(li1,li2)
# li1.append(4)   #这里也是只改变li1不改变li2
# print(li1,li2)


def clone_runoob(li1):
    li_copy = li1[:]  #这个截取赋值实际上是截取出来之后放到了新的一块空间里
    return li_copy    #因此这样复制后列表和原始列表就不再是一个了，不会互相影响，实现真正的复制。
 
li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)