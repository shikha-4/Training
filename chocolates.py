n=int(input("number of packets:"))
a=[]
b=[]
c=[]
d=0
for i in range(n):
    m=int(input())
    a.append(m)
print(a)
for i in range(n):
    if a[i]==0:
        d+=1
        c.append(a[i])
    else:
        b.append(a[i])
print(b+c)
print("number of empty packets:"+str(d))