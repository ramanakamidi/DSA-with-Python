#swap two numbers using bitwise  operators
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a)
print(b)