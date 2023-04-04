def is_anagram(str1, str2):
    str3 = list(str1) #将字符串转化为列表，列表可以对其中的元素进行排序
    str4 = list(str2)
    str3.sort()       #排序，按照ascii码的大小
    str4.sort()
    str3 = ''.join(str3)   #排完序之后再把列表转换为字符串
    str4 = ''.join(str4)   #这个表示把str4列表连成字符串，且中间用''分割，也就是直接相连
    return str3 == str4

