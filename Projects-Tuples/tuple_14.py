# Write a program to input n numbers from the user. Store these numbers in a tuple. Print the maximum and minimum number from this tuple. 


#Program to input n numbers from the user. Store these numbers
#in a tuple. Print the maximum and minimum number from this tuple.
numbers = tuple() #create an empty tuple 'numbers'
n = int(input("How many numbers you want to enter?: "))
for i in range(0,n):
    num = int(input())
    #it will assign numbers entered by user to tuple 'numbers'
    numbers = numbers +(num,)

print(f'The numbers in The Tuple are: \n{numbers}\nThe maximum Number is: {max(numbers)}\nThe minimum Number is: {min(numbers)}')
