#coin match
def fun(li,i,k):
    if k==0:
        return True
    if i<0:
        return False
    if li[i]>k:
        return fun(li,i-1,k)
    return fun(li,i-1,k-li[i]) or fun(li,i-1,k) 
li=[1,2,3,8]
k=9

print(fun(li,len(li)-1,k))