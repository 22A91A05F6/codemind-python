import math
a=input()
a=a.split(":")
h=int(a[0])
m=int(a[1])
a=abs((30*h)-(5.5*m))
b=360-a
if a<b:
    print(f"{a:.1f}")
else:
    print(f"{b:.1f}")