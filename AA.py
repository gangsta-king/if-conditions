n=[input(),input(),input()]
c=0
c1=0
for i in n:
    if int(i)%2==0:
        c+=1
    if int(i)%2==1:
        c1+=1
print('YES' if c>=1 and c1>=1 else 'NO')