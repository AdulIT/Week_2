amount = int(input())
if 5 <= amount % 10 <= 9 or amount % 10 == 0 or amount // 10 == 1:
    print(amount, 'korov')
elif amount % 10 == 1:
    print(amount, "korova")
else:
    print(amount, "korovy")
