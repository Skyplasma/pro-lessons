num = int(input("Number Now! "))

if num % 4 == 0 or (num % 400 == 0 and num % 100 != 0):
    print("true yeapyear")
else:
    print("false yeapyear")
