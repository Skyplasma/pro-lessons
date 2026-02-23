numbers = [
    12, 7, 19, 4, 25,
    8, 16, 3, 42, 9,
    14, 6, 21, 5, 18,
    27, 11, 30, 2, 17,
    23, 10, 35, 1
]



def total(Num_list):
    running_total = 0
    for current_value in Num_list:
        running_total += current_value 
    return running_total

def average(total):
    ave = 0 
    ave = total / len(numbers)
    return ave


print(f"the average value of all numbers is {average(total(numbers))}.")
print(f"the sorted list is {sorted(numbers)}")
print(len(numbers))