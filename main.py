print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()
# 🚨 Don't change the code above 👆
bill = 0
if size == "S":
  #print(" Medium pizza is £15") 
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "y":
 if size == "S":
  bill += 2

else:
 bill += 3

if extra_cheese == "y":
  bill += 1

print(f" Your Final Bill is £{bill}")
print(" Thank you for ordering from Python Pizza Deliveries")