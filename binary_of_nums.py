#binary of nums
def binary(n,res=""):
    if n==0:
        print(res)
        return
    binary(n-1,res+"0")
    binary(n-1,res+'1')
n=4
binary(n)