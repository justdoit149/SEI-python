n = int(input())
num = list(map(int,input().split("\n")))
sum = 1

for i in range(1,n):
    if num[i-1] != num[i]:
        sum = sum + 1
print(sum)