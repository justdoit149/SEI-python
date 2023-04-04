def process(param):
    LEN = len(param)
    for i in range(LEN - 1, -1, -1):  # 注意如果直接删除，那么后面的会补到前面来，导致出现下标问题。
        if len(param[i]) == 1:  # 因此本题选择从后往前删除。且不能用-1到-LEN-1，同样会出现下标问题
            del param[i]  # 因为删掉一个之后从右往左数的位置也改变了
    LEN = len(param)
    s = ','.join(param).title()  # 把原列表相连，空格分隔，然后对字符串进行title（每个单词首字母大写）
    return s


print(process(["cSioDsd", "XOISjc", "coFox", "x", "xcd"]))
