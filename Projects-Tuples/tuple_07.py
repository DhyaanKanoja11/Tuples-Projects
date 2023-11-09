tup=()
c=0
n=int(input("Enter The Range of Elements: "))

for i in range(1,n+1):
    p=int(input(f"Enter Element #{i}: "))
    tup=tup+(p,)
print(tup)
