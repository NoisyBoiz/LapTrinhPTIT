while(1):
    try:
        string = input().strip()
        if(string == ""): break
        arr = list(map(int,string.split(",")))  
        for i in range(max(arr)):
            if(i not in arr):
                print(i)
                break
        else: print(max(arr)+1)
    except EOFError:
        break

