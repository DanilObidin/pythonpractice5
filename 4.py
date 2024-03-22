a = int(input())
b = a % 10
if 5 <= a <= 20:
    print(f"{a} попугаев")
elif b == 1:
    print(f"{a} попугай")
elif b == 2 or b == 3 or b == 4:
    print(f"{a} попугая")
else:
    print(f"{a} попугаев")
