hexa="0123456789ABCDEF"
s=''
n=int(input("number:"))
while n>0:
    s+=hexa[n%16]
    n//=16
print(s[::-1])