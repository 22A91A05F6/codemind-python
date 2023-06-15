n=int(input())
lst=list(map(int,input().split()))
odd=0
for i in lst:
    if i%2!=0:
        odd=odd+1
if odd<=2:
    print("YES")
else:
    print("NO")