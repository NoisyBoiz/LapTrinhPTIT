t = int(input())
for _ in range(t):
    x = input()
    rs = ""
    i = 0
    arr = []
    while i < len(x):
        if(x[i]=="["): arr.append(x[i])
        elif(x[i].isnumeric()):
            k = ""
            while x[i].isnumeric():
                k += x[i]
                i += 1
            i-=1
            arr.append(k)

        elif(x[i]=="]"):
            key = ""
            while(arr[-1]!="["):
                key = arr.pop() + key
            arr.pop()
            if(len(arr) > 0 and arr[-1].isnumeric()):
                arr.append(key*int(arr.pop()))
            else:
                arr.append(key)
        else:
            arr.append(x[i])
        i+=1
    for i in arr:
        rs += i
    print(rs)
