password = input("Enter the password: ")
num_of_asterisks = len(password)

while num_of_asterisks <= 0:
    print("invalid input")
    password = input("Enter the password: ")
    num_of_asterisks = len(password)

print(num_of_asterisks * "*")