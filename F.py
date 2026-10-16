a,b,n=int(input()),int(input()),int(input())
if (n%b==0 and n//b < a) or (n%a==0 and n//a < b):
    print('YES')
else:
    print('NO')