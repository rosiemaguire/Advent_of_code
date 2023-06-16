#  --- Day 1: Calorie Counting ---
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def read_file_as_nested_list(file):
    with open(file) as file:
        day1_input = file.read()
    calories_list = []
    for item in list(day1_input.split(' ')):
        calories_list.append(item.split('\n\n'))
    nested_list = []
    for calories in calories_list:
        output = []
        for calorie in calories:
            output.append(calorie.split('\n'))
        nested_list.extend(output)
    return nested_list


def get_max_value_and_index(nested_list):
    summed_lists = []
    for nest in nested_list:
        count = 0
        for item in nest:
            count += int(item)
        summed_lists.append(count)
    max_value = max(summed_lists)
    return max_value

print(get_max_value_and_index(read_file_as_nested_list("day1_input.txt")))
