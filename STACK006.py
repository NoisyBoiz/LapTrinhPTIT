t = int(input())
for _ in range(t):
    x = input()
    while True:
        ck = 0
        i = 0
        rs = ""
        while i < len(x):
            if(i==0): 
                rs += x[i]
            else:
                if(x[i] == x[i-1]):
                    rs = rs[:-1]
                    ck = 1
                else:
                    rs += x[i]  
            i+=1    
        if(ck==0): break
        x = rs

    print(x)