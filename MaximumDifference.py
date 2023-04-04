a = input().split()
len_a = len(a)
i, j = 0, 0
max_delta = -1
while i < len_a - 1:
    j = i + 1
    while j < len_a:
        if int(a[i]) < int(a[j]):
            d = int(a[j]) - int(a[i])
            if d > max_delta:
                max_delta = d
        j = j + 1
    i = i + 1

print(max_delta,end='')
