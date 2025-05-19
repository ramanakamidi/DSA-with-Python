#prime using recursion
def prime(n,i=2):
    if n<2:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    
    return prime(n,i+1)
n=int(input("enter a num to check Prime"))
print(prime(n))