x,y,z,i=int(input()),int(input()),int(input()),int(input())
if (x==z and y!=i) or (y==i and x!=z) or z-x==i-y or x+y==z+i:
    print('YES')
else:
    print('NO')