x = int(input())
if x%10 == x//1000 and x//10%10 == x//100%10:
    print("настоящее")
else:
    print("кривое")