def is_prime(n):
    if n<2:
            return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
        
        
        
r=int(input("enter rows:"))
c=int(input("eneter columns"))
matrix=[]
if r==c:
    for i in range(r):
        row=list(map(int,input().split()))
        matrix.append(row)
    
sum=0
count=0
for i in range(r):
    for j in range(c):
        if is_prime(matrix[i][j]):
            print(matrix[i][j])
            count+=1
print(count)