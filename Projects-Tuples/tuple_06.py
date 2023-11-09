# Function to check if a student passed or failed
def check_result(average):
    if average > 32:
        return 'Pass'
    else:
        return 'Fail'

# Initialize an empty list to store student names
names = []

# Initialize an empty list to store student data in tuples
student_data = []

n = int(input("Enter the number of students: "))

# Input student data and store it in tuples
for i in range(1, n + 1):
    name = input(f'Enter Name #{i}: ')
    names.append(name)
    total_marks = int(input('Enter Total Marks: '))
    average = float(input('Average: '))
    result = check_result(average)
    t = (name, total_marks, average, result)
    student_data.append(t)

pattern = '#' * 50

while True:
    print(f'\n{pattern}| M E N U |{pattern}')
    print('\n1. Accept\n2. Display\n3. Search\n4. Merit List\n5. Exit')
    choice = int(input('Enter your Choice: '))

    if choice == 1:
        # Display student names and their results
        for data in student_data:
            print(f'{data[0]} - {data[2]}')
            print(f'Result: {data[3]}')

    elif choice == 2:
        # Display all student data in a tabular format
        print('Name\tTotal Marks\tAverage\tResult')
        for data in student_data:
            print(f'{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}')

    elif choice == 3:
        name_to_search = input('Enter Name to search: ')
        if name_to_search in names:
            print('Name\tTotal Marks\tAverage\tResult')
            pos = names.index(name_to_search)
            data = student_data[pos]
            print(f'{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}')

    elif choice == 4:
        print('MERIT LIST')
        for data in student_data:
            if data[2] > 74:
                print(data[0])

    elif choice == 5:
        print('Exiting.............')
        break

    else:
        print('Invalid choice! Try again...')
