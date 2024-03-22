a = int(input())
if a >= 1000 and a <= 9999 and a != (1900, 2051):
    a = str(a)
    if a[0] != a[1] and a[0] != a[2] and a[0] != a[3] and a[1] != a[2] and a[1] != a[3] and a[2] != a[3]:
        print("ok")
    else:
        print("error")

