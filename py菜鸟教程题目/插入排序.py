# 插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
# 它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i]   #暂存待排序的第i个变量
        j = i-1
        while j >=0 and key < arr[j] :   #0~i-1个变量已经排好序
            arr[j+1] = arr[j]            #如果key比当前j位置的还小，就把j位置往后移动一位，并j--
            j -= 1
        arr[j+1] = key 
  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("排序后的数组:") 
for i in range(len(arr)): 
    print ("%d" %arr[i], end = ' ')