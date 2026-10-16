a = int(input())
b = int(input())
c = int(input())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a + b <= c:
    print("impossible")
else:
    if a**2 + b**2 == c**2:
        print("right")
    elif a**2 + b**2 > c**2:
        print("acute")
    else:
        print("obtuse")