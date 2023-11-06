t=tuple()

n=int(input("Enter A Range: "))

for i in range(n):
    a=input(f"Enter Element #{i}: ")
    t= t+(a,)

print(f'The tuple is : {t}')

for i in t:
    print (i)
