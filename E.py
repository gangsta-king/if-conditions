x,y,z,i=int(input()),int(input()),int(input()),int(input())
if (abs(z-x)==2 and abs(i-y)==1) or (abs(i-y)==2 and abs(z-x)==1):
    print('YES')
else:
    print('NO')