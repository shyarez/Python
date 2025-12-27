# logical operators -> evaliuate multiple conditions (or, and, not)
#  or -> one of 2 condn is true
#  and -> both the condn must be true
#  not -> negation of the condn

temp = 26
is_sunny = False
# if temp > 35 or temp < 0 or is_sunny:
#    print("We can go out!")


# if temp >=28 and is_sunny:
 #  print("It is HOT outside")  
 
if 28 > temp > 0 and not is_sunny:
    print("Warm Day")   