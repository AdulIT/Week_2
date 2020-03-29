column1 = int(input())
ceil1 = int(input())
column2 = int(input())
ceil2 = int(input())
if abs(column1 - column2) <= 1 and abs(ceil1 - ceil2) <= 1:
    print('YES')
else:
    print('NO')
