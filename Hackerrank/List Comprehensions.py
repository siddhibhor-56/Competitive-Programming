# Q=https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
arr=[]
p=0
for i in range( x + 1):
     for j in range( y + 1):
        for z in range(z+1):
            if ( ( i + j +z) != n ):
                arr.append([])
                arr[p]=[i,j,z]
                p +=1
print(arr)