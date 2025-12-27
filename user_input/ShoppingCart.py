name = input("Enter your name: ")
item = input("Select an item to BUY: ")
price = float(input("The price is: ₹"))
quantity = int(input("Number of items you would like to buy: "))
total = price * quantity

print(f"You bought {quantity} x {item}/s")
print(f"TOTAL BILL: ₹{total}")