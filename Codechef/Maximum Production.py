# Q=https://www.codechef.com/JULY21C/problems/EITA

try:
    T = int(input())
    while T>0:
        d,x,y,z =map(int,input().split())
        a= x*7
        b =y*d + z*(7-d)
        print(max(a,b))
        T=T+1
except:
    pass