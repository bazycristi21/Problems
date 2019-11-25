

def min(a,b,c):
    if a <= b and a <= c :
        return a
    if b <= c and b <= a:
        return b
    return c

M = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0]
]

n = len(M)
m = len(M[0])
k = 2
for i in range(1,n):
    for j in range(1,m):
        if M[i][j] != 1:
            if M[i-1][j] != 1 and M[i-1][j-1] != 1 and M[i][j-1] != 1:

                minim = min(M[i-1][j], M[i-1][j-1], M[i][j-1])

                if minim == 0:
                    M[i][j] = 2
                else:
                    M[i][j] = minim + 1


for i in M:
    print(i)
maxim = 0
for i in range(1,n):
    for j in range(1,m):
        if M[i][j] > maxim:
            maxim=M[i][j]
            i1 = i
            j1 = j

print(maxim)
print(i1-maxim+1,j1-maxim+1)
k=3
l=0
for i in range(1,n):
    for j in range(1,m):
        if M[i][j] == k:
            l += 1
        if M[i][j] > k:
            l += M[i][j] - k + 1

print(l)
