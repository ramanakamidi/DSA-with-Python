#weight increse
l, b = map(int, input("enter two weights: ").split())
c=0
while l<=b:
    l*=3
    b*=2
    c+=1
print("years=",c)