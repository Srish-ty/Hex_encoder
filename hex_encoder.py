#ascii to binary
chara=input()
bina=""
for c in chara:
    ascival=ord(c)
    #print(ascival," ")
    bin=0
    for i in range(9):
        bin+=ascival%2
        bin/=10
        ascival=ascival//2
    bin*=1000000000
    bin+=0.001
    bin=int(bin)
    leng=len(str(bin))
    if leng<8:
        bina+=("0"*(8-leng)+str(bin))
    else:
        bina+=str(bin)
    
#print(bina)
line = bina
lis=[line[i:i+4] for i in range(0, len(line), 4)]
#print(lis)

res=0
for li in lis:
    res*=10
    for i in range(4):
        res+=int(li[i])*(2**(3-i))
    
    
print(res)   
        