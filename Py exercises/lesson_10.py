import sys

num1 = int(input("num1? "))
dividend = input("dividend? ")
divisor = input("divisor? ")

#if divisor == 0:
#    print("Undefind")
#    exit(1)

if num1 >0:
    print("Positive")
else:
    print("Negative")


try:
    dividend = int(dividend)
    divisor = int(divisor)
    floor_quotient = dividend // divisor
except ZeroDivisionError as i:
    print("ohno. zero div error...")
    print(i)
    exit(7)
except ValueError:
    print("im pretty sure thats not a number...")
    exit(7)
else:
    print("ITS ALIVE!")
finally:
    print("this happens at the the end no matter what...")

print(f"answer rounded down {floor_quotient}")