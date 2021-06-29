# Q = https://www.codechef.com/LRNDSA01/problems/LAPIN

def check(s1,s2):
    count=0
    for i in s1:
        if i in s2:
            if (s1.count(i)==s2.count(i)):
                count=count+1
    if count==len(s1):
        return True
    else:
        return False
        
for _ in range(int(input())):
    s = str(input())
    x = len(s)
    y = int(x/2)
    if x%2==0:
        s1 = s[:y]
        s2 = s[y:]
    else:
        s1 = s[:y]
        s2 = s[y+1:]
    if check(s1,s2):
        print("YES")
    else:
        print("NO")