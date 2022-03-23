#ASCII to binary
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
    
#prints binary code    
#print(bina)

#let's convert that binary into hexadecimal


line = bina
lis=[line[i:i+4] for i in range(0, len(line), 4)]


hexal="ABCDEF"
res=""

for li in lis:
    j=0
    for i in range(4):
        j+=int(li[i])*(2**(3-i))
    #print(j)
    if j<10:
        res+=str(j)
    else:
        res+=hexal[j-10]

    
print(res)   