n = int(input())
s = int(n/29)
g = int(n/493)
if n == 0:
    print("error")
else:
    print(f"{g} галлеонов")
    print(f"{n%s} кнатов")
