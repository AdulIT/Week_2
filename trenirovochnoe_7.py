column1 = int(input())
ceil1 = int(input())
column2 = int(input())
ceil2 = int(input())
if column1 <= column2 and ceil1 <= ceil2:
    if column1 % 2 == 1 and ceil1 % 2 == 1:
        if column2 % 2 == 1 and ceil2 % 2 == 1:
            print("Yes")
        elif column2 % 2 == 0 and ceil2 % 2 == 0:
            print('Yes')
        else:
            print('No')
    elif column1 % 2 == 0 and ceil1 % 2 == 0:
        if column2 % 2 == 1 and ceil2 % 2 == 1:
            print("Yes")
        elif column2 % 2 == 0 and ceil2 % 2 == 0:
            print('Yes')
        else:
            print('No')
else:
    print('No')
