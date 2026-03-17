n = input("What is your name? ")
print(f"Hello, {n}")

if n == "Joe":
    print("Welcome, superuser!")
else:
    print("Hello, regular user.")

How to normalize input
we use strip() to remove leading/trailing whitespace
incorrect_name = " Joe     "
print(f"Incorrect: >{incorrect_name}<")

corrected_name = incorrect_name.strip()
print(f"Corrected: >{corrected_name}<")

we use capitalize() to capitalize our name
incorrect_name = "joe"
print(f"Incorrect: >{incorrect_name}<")

corrected_name = incorrect_name.capitalize()
# Opposite of capitalize is lower()
print(f"Corrected: >{corrected_name}<")

Functions we have so far:
strip() - remove spaces
capitalize() - capitalize first letter
lower() - lowercase all letters
upper() - uppercase all letters

incorrect_name = "kayleigh"
print(f"Incorrect: >{incorrect_name}<")

corrected_name = incorrect_name.upper()
print(f"Corrected: >{corrected_name}<")

First Problem
print("First problem")
# We convert a string to a list
party_guests = "john , mary,FRED,seBastian,isaak" # This needs some work
party_list = ["john", "mary"]                   # This works immediately

party_guests_converted = party_guests.split(",") # This makes the string work!

def clean_name(incorrect_name):
    corrected_name = incorrect_name.strip()
    corrected_name = corrected_name.capitalize()
    return corrected_name

for guest in party_guests_converted:
    guest = clean_name(guest)
    print(f"Hi, {guest}, you are invited!")

# Second Problem
print("\n\nSecond problem")
# We convert a list to a string
party_list = ["john", "mary", "nicholas"]
print(f"Hi, {", ".join(party_list)}")

# Third problem
n = input("What is your name? ")
if n != "Luca":
    print("Your name is not Luca!")

if "u" in n:
    print("Your name has the letter u in it!")

# Look at these names:
# Albert
# Alberto
# Alberta
# Albertini

if n.startswith("Albert"):
    print("Your name starts with Albert!")

if n.endswith("e"):
    print("Your name ends with e!")
