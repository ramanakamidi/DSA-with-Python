def Xor(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
l=int(input("ennetr:"))
r=int(input("ennetr:"))
a=Xor(r)
b=Xor(l-1)
print(a^b)