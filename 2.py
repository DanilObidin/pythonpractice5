xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
a = x - xc
b = y - yc
c = (a**2 + b**2)**0.5
if c > r:
    print("вне окружности")
if r > c:
    print("в окружности")
