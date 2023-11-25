import math

def check(i):
    if(i<2): return False
    for j in range(2,(int)(math.sqrt(i))+1,1):
        if(i%j == 0):
            return False
    return True

t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    rs = 0
    for i in range(n,k+1):
        if(check(i)):
            rs += i
    print(rs)
  