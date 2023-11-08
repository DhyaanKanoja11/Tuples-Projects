tup=()
c=0
n=int(input("Enter The Range of Elements: "))

for i in range(1,n+1):
    p=int(input(f"Enter Element #{i}: "))
    tup=tup+(p,)
print(tup)

x=int(input("Enter What You Want To Search in The List: "))

if x in tup:
    print("Element Found")


print(f"{x} was found {c} times in {tup}")