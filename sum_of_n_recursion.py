
def fun(n):
    if n==0:
        return 0
    return n+fun(n-1)

print(fun(5))


def fun(n,sum):
    if n==0:
        print(sum)
        return
    fun(n-1,sum+n)
fun(4,0)