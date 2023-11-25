import math

NTWMap1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NTWMap2 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen","eighteen", "nineteen"]
NTWMap3 = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]
NTWMap4 = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion","sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", "duodecillion","tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion","octodecillion", "novemdecillion", "vigintillion"]

def NumToWord(n):
    if(int(n) < 10): return NTWMap1[int(n)-1]
    elif(int(n) <20): return NTWMap2[int(n[1])-1]
    elif(int(n) <100): 
        if(int(n[1])==0): return NTWMap3[int(n[0])-1]
        else: return NTWMap3[int(n[0])-1] + " " + NTWMap1[int(n[1])-1]
    else:
        if(int(n[1:])==0): return NTWMap1[int(n[0])-1] + " " + NTWMap4[0]
        else: return NTWMap1[int(n[0])-1] + " " + NTWMap4[0] + " " + NumToWord(n[1:])

t = int(input())
for _ in range(t):
    n = input()
    rs = ""
    l = math.ceil(len(n)/3)
    for i in range(l):
        if(i==l-1): rs = NumToWord(n[-3:]) + " " + NTWMap4[i] + " " + rs
        else: rs = NumToWord(n[-3:]) + " " + rs
        n = n[:-3]
    print(rs.strip().capitalize())



