t = int(input())
for _ in range(t):
    x = input()
    dic = {}
    arr = []
    i = 0
    while i < len(x):
        if(x[i]=="("): arr.append((x[i],0))
        elif(x[i]==")"): 
            k=1
            if(i!=len(x)-1 and x[i+1].isnumeric()): 
                k = int(x[i+1])
                i+=1

            add = []
            while arr[-1][0] != "(":
                key, c = arr.pop()
                add.append((key,k*c))
            arr.pop()
            
            while len(add) != 0:
                arr.append(add.pop())

        elif(x[i].isalpha()):
            if(x[i].isupper()):
                arr.append((x[i],1))
            elif(x[i].islower()):
                key, c = arr.pop()
                arr.append((key+x[i],c))

        else:
            k = int(x[i])
            key, c = arr.pop()
            arr.append((key,k*c))
        i+=1
    
    for i in arr:
        if(i[0] not in dic):
            dic[i[0]] = i[1]
        else:
            dic[i[0]] += i[1]
            
    dic = sorted(dic.items(),key=lambda x: x[0])
    for i in dic:
        if(i[1]==1): print(i[0],end="")
        else: print(i[0]+str(i[1]),end="")
    print()
            
    