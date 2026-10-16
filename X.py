n=int(input())
an1,an5,an10,an20,an60=0,0,0,0,0
maxav=999999
for c60 in range(n//60+2):
    for c20 in range(n//20+2):
        for c10 in range(n//10+2):
            for c5 in range(n//5+2):
                totalr=c60*60+c20*20+c10*10+c5*5
                if totalr>=n:
                    c1=0
                else:
                    c1=n-totalr
                totcount=c60*440+c20*230+c10*125+c5*70+c1*15

                if totcount<maxav:
                    maxav=totcount
                    an1=c1
                    an5=c5
                    an10=c10
                    an20=c20
                    an60=c60
print(an1,an5,an10,an20,an60)