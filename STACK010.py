t = int(input())

for _ in range(t):
    n = int(input())
    d = 0
    arr = []
    rs = n
    for i in range(n,0,-1):
        if(d%4==0): rs = i
        elif(d%4==1): rs *= i
        elif(d%4==2): rs //= i
        elif(d%4==3): 
            arr.append(rs)
            arr.append(i)
            rs = 0
        d += 1
    if(rs!=0): arr.append(rs)
    rs = arr[0]
    for i in range(1,len(arr)):
        if(i%2==1): rs += arr[i]
        else: rs -= arr[i]
    print(rs)