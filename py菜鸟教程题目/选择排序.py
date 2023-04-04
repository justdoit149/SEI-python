A = [64, 25, 12, 22, 11] 
  
for i in range(len(A)): #python可以这样写，只算一次len；但是c严禁这样写，会算len次len
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
                
    A[i], A[min_idx] = A[min_idx], A[i]  #python交换变量比较灵活，它把原变量都复制了一份之后放进去
  
print ("排序后的数组：") 
for i in range(len(A)): 
    print("%d" %A[i], end = ' ')