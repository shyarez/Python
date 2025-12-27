# input() - A function that prompts the user to enter data
#           It returns the entered data as a string

email = input("Enter your email: ")
age = input("Enter your age: ")

age = int(age)
age += 1

print(f"Your email is {email}")
print("HAPPY BIRTHDAY")
print(f"Your age is {age}")

# Note - Strings cannot be used with arithmetic expressions,
# else it will show an error
# we will need to typecast it to an int() or float()

# You can also condense your code for better readability by doing :
# age = int(input("Enter your age: ")) ✅✅