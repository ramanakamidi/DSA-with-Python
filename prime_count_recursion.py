def is_prime(n,i=2):
    if n<2:
        return 0
    if n==2:
        return 1
    if n%i==0:
        return 0
    if i*i>n:
        return 1
    return is_prime(n,i+1)

li=list(map(int,input("enter a list: ").split()))

def p_count(li,i=0):
    if i==len(li):
        return 0
    if is_prime(li[i]):
        print(li[i])
        return 1+p_count(li,i+1)
    return p_count(li,i+1)
print(p_count(li))