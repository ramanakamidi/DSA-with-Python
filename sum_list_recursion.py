#sum of list
li=list(map(int,input().split()))

def fun(li,i=0):
    if i==len(li):
        return 0
    return li[i]+fun(li,i+1)
print(fun(li))