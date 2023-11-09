tup=()

n=int(input("Enter The Range of Elements: "))

for i in range(1,n+1):
    p=input(f"Enter Element #{i}: ")
    tup=tup+(p,)

lst=[]
p=()
print(f"The Tuple Created is {tup}")

lst.append(tup[0])
lst.append(tup[1])
lst.append(tup[-2])
lst.append(tup[-1])

p=tuple(lst)

print(f"The New List Created is {p}")
