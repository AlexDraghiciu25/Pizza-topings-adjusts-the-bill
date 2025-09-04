print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
ok_size = 1

if size == "S" or size == "M" or size == "L":
    ok_size = 1
else:
    ok_size = 0

while ok_size == 0:
    if ok_size == 0:
        size = input("You should type a letter(S/M/L) until it is a correct one!\n")

    if size == "S" or size == "M" or size == "L":
        ok_size = 1

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
ok_pepperoni = 1

if pepperoni == "Y" or pepperoni == "N":
    ok_pepperoni = 1
else:
    ok_pepperoni = 0

while ok_pepperoni == 0:
    if ok_pepperoni == 0:
        pepperoni = input("You should type a letter(Y/N) until it is a correct one!\n")

    if pepperoni == "Y" or pepperoni == "N":
        ok_pepperoni = 1

extra_cheese = input("Do you want extra cheese? Y or N: ")
ok_extra_cheese = 1

if extra_cheese == "Y" or extra_cheese == "N":
    ok_extra_cheese = 1
else:
    ok_extra_cheese = 0

while ok_extra_cheese == 0:
    if ok_extra_cheese == 0:
        extra_cheese = input("You should type a letter(Y/N) until it is a correct one!\n")

    if extra_cheese == "Y" or extra_cheese == "N":
        ok_extra_cheese = 1

bill = 0
if size == "S":
    if pepperoni == "Y":
        bill += 2
    bill += 15
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")