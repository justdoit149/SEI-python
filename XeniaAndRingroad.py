line1 = input().split()
line2 = input().split()
n = int(line1[0])
m = int(line1[1])
a = [1]
sum = 0
for i in range(m):
    a.append(int(line2[i]))
for i in range(m):
    if a[i+1] >= a[i]:
        sum = sum + a[i+1] - a[i]
    else:
        sum = sum + n + a[i+1] - a[i]
print(sum)