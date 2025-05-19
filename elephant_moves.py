#elephant moves 1,2,3,4,5
n=int(input())
steps=0
if n<=5:
    print("steps=1")
elif n%5==0:
    print("steps=",n//5)
else:
    print("steps=",n//5+1)