k = int(input())
m = int(input())
n = int(input())
if k == n:
    print(m * 2)
elif n % k == 0:
    print(n // k * m * 2)
elif k > n:
    print(m * 2)
else:
    print(((n * 2 - 1) // k + 1) * m)
