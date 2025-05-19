#find unique number with bitwise except one all are twice
li=list(map(int,input().split()))
x=0
for i in li:
    x=x^i
print(x)