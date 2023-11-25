t = int(input())
for _ in range(t):
    arr = list(map(int,input().split(",")))
    n = 1
    for i in arr:
        n *= i
    for i in range(len(arr)):
        print(n//arr[i],end="," if i!=len(arr)-1 else "\n")