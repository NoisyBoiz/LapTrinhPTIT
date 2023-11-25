t = int(input())

for _ in range(t):
    string = input()
    st = []
    i = 0
    while i < len(string):
        if(string[i] == "("): st.append(string[i])
        elif(string[i] == ")"):
            key = ""
            while(st[-1]!="("):
                key = st.pop() + key
            st.pop()
            key = key[::-1]
            st.append(key)
        else:
            st.append(string[i])
        i+=1
    for i in st:
        print(i,end="")
    print()
    