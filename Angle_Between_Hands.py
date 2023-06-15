import math
a=input()
a=a.split(":")
h=int(a[0])
m=int(a[1])
c=abs((30*h)-(5.5*m))
b=360-c
if c<b:
    print(f"{c:.1f}")
else:
    print(f"{b:.1f}")