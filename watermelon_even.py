w=int(input("enter the weight of watermelon"))
if w%2!=0 or w==2:
    print("NO")
else:
    x=w//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)