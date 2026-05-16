num=int(input("enter the number:"))
l=len(str(num))
n=num
sum=0
for i in range(l):
    r=n%10
    sum+=r**l
    n//=10
print(sum)
if sum==num:
    print("amstrong")
else:
    print("not")
