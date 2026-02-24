import sys

num1 = int(input("num1? "))
dividend = int(input("dividend? "))
divisor = int(input("divisor? "))

#if divisor == 0:
#    print("Undefind")
#    exit(1)

if num1 >0:
    print("Positive")
else:
    print("Negative")


try:
    floor_quotient = dividend // divisor
except ZeroDivisionError:
    print("ohno. zero div error...")
    exit(7)

print(f"answer rounded down {floor_quotient}")