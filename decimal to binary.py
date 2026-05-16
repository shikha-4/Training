'''n=int(input("number:"))
print(bin(n))'''

''' OR '''
s=''
n=int(input("number:"))
while n>0:
    s+=str(n%2)
    n//=2
print(s[::-1])
      