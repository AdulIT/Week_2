num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 == num3:
    print("3")
elif num1 == num2 != num3:
    print("2")
elif num1 == num3 != num2:
    print("2")
elif num2 == num3 != num1:
    print("2")
else:
    print("0")
