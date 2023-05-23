n=int(input())
s=0
t=0
sq=n*n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
rsq=s*s
while rsq>0:
    r=rsq%10
    t=t*10+r
    rsq=rsq//10
if sq==t:
    print("True")
else:
    print("False")