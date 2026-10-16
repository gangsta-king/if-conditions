#  ( ax + b ) : ( cx + d ) = 0.
a,b,c,d = int(input()),int(input()),int(input()),int(input())
if a==0 and b==0:
    print('INF')
elif a==0 or b % a != 0:
    print('NO')
else:
    x = -b // a
    if c * x + d == 0:
        print('NO')
    else:
        print(x)