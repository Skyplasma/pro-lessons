int1 = int(input("adsfadfsadsf"))
int2 = int(input("asdfasdfasdf"))

print(f"{int1}  {int2}")

def what(x):
    if x < 0:
        print(f"{x} is neg")
    elif x > 0:
        print(f"{x} is pos")
    else:
        print(f"{x} is zero")

def who(x):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def why(x,z):
    if x > z:
        print(f"{x} is greater than {z}")
    elif x < z:
        print(f"{x} is less than {z}")
    else:
        print(f"{x} is equal to {z}")

def gravity(x,z):
    print(x + z)
    print(abs(x - z))
    print(x * z)



what(int1)
what(int2)
who(int1)
who(int2)
why(int1,int2)
gravity(int1,int2)
