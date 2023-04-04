
def histogram(fileName):
    f = open(fileName)
    n = int(f.readline())
    nums = list(map(int,f.readline().split()))     #list(map(function,list))
    ranges = [0,0,0,0,0,0,0,0,0,0]
    for i in range(n):
        index = min(nums[i] // 10, 9)
        ranges[index] = ranges[index] + 1
    print(",".join(list(map(str,ranges))))
    for i in range(9):
        print("{0:>2} - {1:>2}:".format(i*10,i*10+9) + "*" * ranges[i])
    print("{0:>2} -{1:>3}:".format(90,100) + "*" * ranges[9])
    return