x = float(input())
y = float(input())
days = 1
while x < y:
    x = x + x / 10
    days += 1
print(days)
