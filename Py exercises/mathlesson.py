def doubleAddOne(x):
    print(2 * x + 1)

def twentyPercentOff(price):
    return price * 0.8

def GSTadd(price):
    return price * 1.1

coke = 2.5
coke_with_tax = GSTadd(coke)
cokefinal = twentyPercentOff(coke_with_tax)

print(f"final price {cokefinal}")
