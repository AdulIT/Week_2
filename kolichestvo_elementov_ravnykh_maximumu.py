maximum = 0
num_max = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_max = element, 1
    elif element == maximum:
        num_max += 1
print(num_max)
