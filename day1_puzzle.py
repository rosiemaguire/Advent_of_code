with open('day1_input.txt','r') as file:
    day1_input = file.read()
a = list(day1_input.split(' '))

# print(a)
calories = []

for item in a:
    calories2 = item.split('\n\n')
    calories.append((calories2))

output = []
for item in calories:
    calories3 = []
    for item2 in item:
        calories3.append(item2.split('\n'))
    output.append(calories3)
print(output)