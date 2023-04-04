def move(UDLR, pace, last):
    global x,y,errors
    if errors == 1:
        return
    if UDLR == 'R':
        if y + pace > 9 or y + pace < 0:
            print("Error!")
            errors = 1                               
            return                
        for j in range(pace):
            y = y + 1
            if pen == True:
                qipan[x][y] = last
    elif UDLR == 'L':
        if y - pace > 9 or y - pace < 0:
            print("Error!")
            errors = 1
            return
        for j in range(pace):
            y = y - 1
            if pen == True:
                qipan[x][y] = last
    elif UDLR == 'U':
        if x - pace > 9 or x - pace < 0:
            print("Error!")
            errors = 1
            return
        for j in range(pace):
            x = x - 1
            if pen == True:
                qipan[x][y] = last
    elif UDLR == 'D':
        if x + pace > 9 or x + pace < 0:
            print("Error!")
            errors = 1
            return
        for j in range(pace):
            x = x + 1
            if pen == True:
                qipan[x][y] = last  

def cross(Len,last):
    move('R', Len, last)
    move('L', Len * 2, last)
    move('R', Len, last)
    move('U', Len, last)
    move('D', Len * 2, last)
    move('U', Len, last)

def rect(xlen,ylen,last):
    if pen == True:
        qipan[x][y] = last
    move('R', xlen-1, last)
    move('D', ylen-1, last)
    move('L', xlen-1, last)
    move('U', ylen-1, last)

def rect_f(xlen,ylen,last):
    global x
    x0 = x
    for i in range(ylen):
        rect(xlen,1,last)
        x = x + 1
    x = x0




#初始化
pen = True    #pen为true表示可以画，为false表示不能画
global x,y,errors
x, y = 0, 0                 
last = ' '
errors = 0
qipan = [[] for i in range(10)] 
for i in range(10):
    for j in range(10):
        qipan[i].append(' ')                     


while(1):
    act = input().split()   
    len_of_act = len(act)
    if act[0] == 'end' or errors == 1:
        break
    elif act[0] == 'move':
        if(len_of_act == 4):
            last = act[3]
        move(act[1],int(act[2]),last)
    elif act[0] == 'pen_up':
        pen = False
    elif act[0] == 'pen_down':
        pen = True
    elif act[0] == 'cross':
        if(len_of_act == 3):
            last = act[2]
        cross(int(act[1]),last)
    elif act[0] == 'rect':
        if(len_of_act == 4):
            last = act[3]
        rect(int(act[1]),int(act[2]),last)
    elif act[0] == 'rect_f':
        if(len_of_act == 4):
            last = act[3]
        rect_f(int(act[1]),int(act[2]),last)

if errors == 0:
    for i in range(10):
        for j in range(10):            
            print(qipan[i][j],end = '')  
        print()                          
    