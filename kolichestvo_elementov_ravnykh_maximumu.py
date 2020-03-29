x = int(input())
maxX = x
s = 0
while x != 0:
    if x > maxX:
        maxX = x
        n = 1
    elif x == maxX:
        s = s + 1
    x = int(input())
print(s)
