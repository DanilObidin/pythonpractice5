f = int(input())
if f % 4 == 0 and f % 100 != 0 or f % 400 == 0:
    print("366")
else:
    print("365")