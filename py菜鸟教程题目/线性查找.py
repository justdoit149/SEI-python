# 线性查找指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。

# 由于参数类型不固定，所以可以查列表、字符串、数字等等
# 但好像直接 if x in list: 更加简洁方便
def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i 
    return -1 
  
# 在数组 arr 中查找字符 D
arr = [ 'A', 'B', 'C', 'D', 'E' ] 
x = 'D' 
n = len(arr) 
result = search(arr, n, x) 
if(result == -1): 
    print("元素不在数组中") 
else: 
    print("元素在数组中的索引为", result)