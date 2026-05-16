'''QUESTION  : Binary representation of 10 is 1010. After toggling the bits(1010), 
will get 0101 which represents "5". Hence output will print "5".'''


n=int(input("decimal:"))
#b=print(bin(n))
s=''
a=[]
while n>0:
    p=str(n%2)
    a.append(p)
    s=s+p
    n//=2
print(s[::-1])
t=print(s)
p=len(a)-1
d=0
for i in range(len(a)):
    if a[i]=='1':
        d=d+(2**p)
        p=int(p)-1
    else:
        p=int(p)-1
print(d)