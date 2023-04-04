q = int(input())
for i in range(q):
    s, t = input(), input()
    IsError, index_s, IsSuccess = 0, 0, 0
    LEN_s, LEN_t = len(s), len(t)
    for start in range(LEN_s - LEN_t + 1):
        if s[start] != t[0]:
            continue
        index_s, IsError = start, 0
        for j in range(LEN_t):
            if index_s >= LEN_s:
                IsError = 1
                break
            while t[j] != s[index_s]:
                index_s += 2
                if index_s >= LEN_s:
                    IsError = 1
                    break
            index_s += 1
        if IsError == 0 and (LEN_s - index_s) % 2 == 0:
            print("YES")
            IsSuccess = 1
            break
    if IsSuccess == 0:
        print("NO")


