numbers = [
    12, 7, 19, 4, 25,
    8, 16, 3, 42, 9,
    14, 6, 21, 5, 18,
    27, 11, 30, 2, 17,
    23, 10, 35, 1
]

def even_squares_list(n):
    return [i * i for i in n if i % 2 ==0]

def sum_of_squares_gen(n):
    return sum(i*i for i in n) # generator function apparently

nums = even_squares_list(numbers)

print(nums)