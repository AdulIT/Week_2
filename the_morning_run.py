x = float(input())
y = float(input())
count = 0
while x <= y:
    count += 1
    x = x * 1/10
    x = x + 1
    if count == y:
        break
print(count)