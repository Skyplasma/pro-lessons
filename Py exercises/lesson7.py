a = [1,2,3,4,5]
b = ['A','b','c','d','e']
c = "hello pro gamers I SALUTE YOU HELLDIVER"

print(c)
print(c[0])
print(c[-1])
print(c[4])
print(c[len(c) - 1])

print(list(c))
print(f'length of a {len(a)}')

for element in a:
    print(element)

for claracter in list(c):
    print(claracter)

vowels = list("aeiou")

def countvow(sentence):
    numvowels = 0
    for charazard in list(sentence.lower()):
        if charazard in vowels:
            numvowels += 1
    return  numvowels

print(f"{c} has {countvow(c)} vowels")

empty = []
print(empty)
