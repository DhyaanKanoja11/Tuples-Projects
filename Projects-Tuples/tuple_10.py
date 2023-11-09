# Program to read email IDs of n students, extract usernames and domains,
# and store them in tuples. Prints email IDs, usernames, and domains at the end.

# Get the number of students
n = int(input("Enter the number of students: "))

# Initialize empty tuples to store email IDs, usernames, and domain names
email_ids = ()
usernames = ()
domains = ()

# Read email IDs and extract data
for i in range(n):
    email = input(f"Enter the email ID of student {i + 1}: ")
    
    # Split the email address
    parts = email.split('@')
    
    # Extract username and domain, or mark as 'Invalid' if not in correct format
    username = parts[0] if len(parts) == 2 else 'Invalid'
    domain = parts[1] if len(parts) == 2 else 'Invalid'
    
    # Append values to tuples
    email_ids += (email,)
    usernames += (username,)
    domains += (domain,)

# Print the tuples
print("Email IDs:\n", email_ids)
print("Usernames:\n", usernames)
print("Domains:\n", domains)
