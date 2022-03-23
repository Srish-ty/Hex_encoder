#write ur binary code without any spaces
#this will convert it to hexadecimal


line = str(input())
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
         
        