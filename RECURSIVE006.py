def poww(a,b):
    if(b==0): return 1
    if(b==1): return a
    temp = poww(a,b//2)
    if(b%2==0): return temp*temp
    else: return temp*temp*a

def countGoodNumbers(n):
    return poww(5,(n+1)//2)*poww(4,n//2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(countGoodNumbers(n)%(10**9+7))