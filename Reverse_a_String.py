def reverse(s):
    st=""
    for i in s:
        st=i+st
    return st
s=input()
print(reverse(s))