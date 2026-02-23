numbers = [
    12, 7, 19, 4, 25,
    8, 16, 3, 42, 9,
    14, 6, 21, 5, 18,
    27, 11, 30, 2, 17,
    23, 10, 35, 1
]

print(sorted(numbers))

def total(Num_list):
    print("lol")


def average(Num_list):
    running_total = 0
    ave = 0
    for current_value in Num_list:
        running_total += current_value 
    ave = running_total / len(Num_list)
    return ave


average(numbers)