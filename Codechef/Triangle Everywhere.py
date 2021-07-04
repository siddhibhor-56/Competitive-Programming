Q=https://www.codechef.com/CCSTART2/problems/EXTRICHK

try:
    a,b,c = map(int,input().split())
    if (a+b)>c and (b+c)>a and (a+c)>b:
        if a == b == c:
            print(1)
        elif a==b or b==c or c==a:
            print(2)
        elif a != b != c:
            print(3)
    else:
        print(-1)
except:
    pass