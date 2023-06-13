import math
n=int(input())
s=0
temp=n
while n>0:
    r=n%10
    p=math.factorial(r)
    s=s+p
    n=n//10
if temp==s:
    print(f"The number {temp} is a strong number")
else:
    print(f"The number {temp} is not a strong number")
    