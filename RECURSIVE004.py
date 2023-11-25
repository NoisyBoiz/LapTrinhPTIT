def gcd(x,y):
    if(y==0): return x
    else: return gcd(y,x%y)

t = int(input())
for _ in range(t):
    x,y = sorted(map(int,input().split()))
    print(gcd(x,y))