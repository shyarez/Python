# if -> Do something when the condition is TRUE
# else -> Do something else

age = int(input("Enter your age: "))
if age >= 18 :
    print("ELIGIBLE!")
elif age < 0 :
    print("INVALID AGE!")    
else:
    print("NOT ELIGIBLE!")