t = int(input())
for _ in range(t):
    x,y = input().split()
    arr = list(map(int,x.split(",")))
    brr = list(map(int,y.split(",")))
    rs = []
    for i in arr:
        if i not in rs and i in brr:
            rs.append(i)
    print(",".join(map(str,rs)))
