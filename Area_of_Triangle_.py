a,b,c=map(int,input().split())
s=(a+b+c)/2
m=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"{m:.2f}")