n=int(input())
print(f'{n} korova' if n==1 else f'{n} korovy' if n%10==2 and n!=12 else f'{n} korov')