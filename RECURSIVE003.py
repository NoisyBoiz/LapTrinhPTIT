def isPowerOfFour(n):
    if(n%4!=0): return False
    else:
        if(n==4): return True
        else: return isPowerOfFour(n//4)

t = int(input())
for _ in range(t):
    n = int(input())
    if(isPowerOfFour(n)): print("1")
    else: print("0")