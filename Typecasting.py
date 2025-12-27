# Typecasting - the process of converting a variable from one data type to another 
# str() , int(), float(), bool()

name = "Meer"
age = 21
cgpa = 9.5
is_stud = True

type(name)  # it will determine the datatype of the variable
            # however, if u execute it w/o a print statement it will not work

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_stud))

# for e.g To convert the cgpa(float) to an integer

cgpa = int(cgpa)
age = float(age)
name = bool(name)

print(cgpa)
print(age)
print(name)

