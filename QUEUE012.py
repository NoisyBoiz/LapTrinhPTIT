t = int(input())
for _ in range(t):
    x,y = input().split()
    arr = list(map(int,x.split(",")))
    brr = list(map(int,y.split(",")))
    rs = []
    for i in arr:
        if i not in rs:
            rs.append(i)
    for i in brr:
        if i not in rs:
            rs.append(i)
    print(",".join(map(str,rs)))
