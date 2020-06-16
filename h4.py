import numpy as np
fp = open('plaintexttwo.txt', "wt")
fp.write("Text encryption decryption in python using alternating stop and go generator")
fp.close()
emp = []
op = []
ec = []
dc=[]
z = []
np.array(emp)
fp = open('plaintexttwo.txt', "rt")
for i in fp:
    for a in i:
        val=ord(a)
        while(val>0):
            for z in range(0,7):
                emp.append(val%2)
                val=val//2
fp.close()
lfsr1=[1,0,1]
np.array(lfsr1)
lfsr2=[1,0,1,0]
np.array(lfsr2)
lfsr3=[1,0,1,0,1]
np.array(lfsr3)
op=[]
ec=[]
np.array(op)
np.array(ec)
np.array(dc)
n=len(i)*7+1
for a in range(0,(len(i)*7)):
    x=lfsr1[2]
    z=lfsr2[3]
    y=lfsr3[4]
    k=((lfsr1[0]+lfsr1[2])%2)
    if(x==1):
        z=lfsr2[3]
        c = ((lfsr2[0] + lfsr2[3]) % 2)
        for b in range(2,-1,-1):
            lfsr2[b+1]=lfsr2[b]
        lfsr2[0]=c
    if(x==0):
        y = lfsr3[4]
        w = ((lfsr3[0] + lfsr3[3]) % 2)
        for b in range(3, -1, -1):
            lfsr3[b + 1] = lfsr3[b]
        lfsr3[0] = w
    op.append(z^y)
    for b in range(1,-1,-1):
        lfsr1[b+1]=lfsr1[b]
    lfsr1[1]=k
b=0
print(emp)
print(op)
res=np.bitwise_xor(emp,op)
print(res)
print(ec)
dec=np.bitwise_xor(res,op)
lp = open('newtexttwo.txt', "wt")
lp.write("The Encrypted text is\n")
while(b<len(i)*7):
    d=0
    for j in range(b,b+7):
        d=d+(pow(2,j-b)*res[j])
    ec.append(chr(d))
    b=b+7
print(ec)
for l in ec:
    for k in l:
        lp.write(k)
print("\n")
lp.write("\nThe decrypted text is\n")
m=0
while(m<len(i)*7):
    d=0
    for j in range(m,m+7):
        d=d+(pow(2,j-m)*dec[j])
    dc.append(chr(d))
    m=m+7
print(dc)
for l in dc:
    for k in l:
        lp.write(k)
lp.close()










