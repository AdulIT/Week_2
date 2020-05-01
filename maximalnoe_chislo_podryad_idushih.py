num = -1
current = 0
maxi = 0
x = int(input())
while x != 0:
    if num == x:
        current += 1
    else:
        num = x
        maxi = max(maxi, current)
        current = 1
    x = int(input())
maxi = max(maxi, current)
print(maxi)
