t = int(input())
for _ in range(t):
    n = int(input())
    qe = []
    qe.append((n,0))
    while(len(qe)!=0):
        x,y = qe.pop(0)
        if(x==1):
            print(y)
            break
        if(x%2==0):
            qe.append((x//2,y+1))
        if(x%3==0):
            qe.append((x//3,y+1))
        if(x>1):
            qe.append((x-1,y+1))
