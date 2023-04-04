n = int(input())
num = list(map(int,input().split()))
SUM = sum(num)
SUM2 = 0
LEN = len(num)
for i in range(LEN):
    SUM2 = SUM2 + num[i]
    if SUM2 * 2 > SUM:
        R = SUM - SUM2
        L = SUM2 - num[i]
        if L <= R:
            print(i+1,LEN-i-1)
        else:
            print(i,LEN-i)
        break
    elif SUM2 * 2 == SUM:
        print(i+1,LEN-i-1)
        break