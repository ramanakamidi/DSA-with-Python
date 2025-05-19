#fibonacci series
n = int(input("Enter how many Fibonacci numbers to print: "))
s1 = 0
s2 = 1
i = 0
while i < n:
    print(s1,end=" ")
    next_term = s1 + s2
    s1 = s2
    s2 = next_term
    i += 1


