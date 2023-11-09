#Write a program to swap two numbers without using a temporary variable.
#Program to swap two numbers


num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print("\nNumbers before swapping:")
print("First Number:",num1)
print("Second Number:",num2)
(num1,num2) = (num2,num1)
print("\nNumbers after swapping:")
print("First Number:",num1)
print("Second Number:",num2)