numbers = [
    12, 7, 19, 4, 25,
    8, 16, 3, 42, 9,
    14, 6, 21, 5, 18,
    27, 11, 30, 2, 17,
    23, 10, 35, 1
]

def only_evens(Num_list):
    for number in Num_list:
        if number % 2 == 0:
            yield number

x = only_evens(numbers) #cannot be called directly as is a machine not a value

for i in x:
    print(i)