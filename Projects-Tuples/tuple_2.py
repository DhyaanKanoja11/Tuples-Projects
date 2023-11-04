#Enter 6 element in a tuple and print element who are divisible by only 5 
x=[]
tup=(25,15,1,2,30)

for i in tup:
    if i%5==0:
        print(i)
        x.append(i)
        z=tuple(x)
    else:
        print()
print(z)