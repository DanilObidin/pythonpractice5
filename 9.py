a, b, c = map(int, input().split())
if a > b and a > c and b < c:
    print(a, c, b)
if a > b and a > c and b > c:
    print(a, c, b)
if b > a and b > c and a > c:
    print(b, a, c)
if b > a and b > c and c > a:
    print(b, c, a)
if c > a and c > b and b > a:
    print(c, b, a)
if c > a and c > b and a > b:
    print(c, a, b)