n=int(input())
a=[]
b=[]
d=[]
co=0
for i in range(n):
    c=int(input())
    a.append(c)
print(a)
for i in range(len(a)):
   if a[i]%2==1: 
       b.append(a[i])
       b.sort()
   else:
       d.append(a[i])
       d.sort()
       co=co+1
print(co)