#fibonacci using recursion
def fiboSum(n):
    if n==0 or n==1:
        return n
    return fiboSum(n-1)+fiboSum(n-2)

print(fiboSum(6))