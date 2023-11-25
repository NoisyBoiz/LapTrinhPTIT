t = int(input())
for _ in range(t):
    string = input()
    if(string == string[::-1]): print(1)
    else: print(0)