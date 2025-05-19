#sum of even numbers in odd indexes
li=[2,3,7,5,1,4,6,8,9]
sum=0
for i in range(1,len(li),2):
    if li[i]%2==0:
        sum+=li[i]
print(sum)