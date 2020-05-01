num = -1
max_num = 0
second_max = 0
while num != 0:
    num = int(input())
    if num > max_num and num != 0:
        second_max = max_num
        max_num = num
    elif num > second_max and num != 0:
        second_max = num
print(second_max)
