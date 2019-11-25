M = [
    [3,8,4,3],
    [2,4,2,6],
    [1,7,11,5],
]

A = M

def max3(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

def max2(a,b):
    if a >= b:
        return a
    return b

drum = []

n = len(M)
m = len(M[0])

for j in range(1, m):

    for i in range(0,n):
        maxim = 0
        if i == 0:
            maxim = max2(M[i][j-1],M[i+1][j-1])
        elif i == n-1:
            maxim = max2(M[i][j-1],M[i-1][j-1])
        if i != 0 and i != n-1:
            maxim = max3(M[i][j-1],M[i-1][j-1],M[i+1][j-1])
        M[i][j] += maxim
maxim2 = 0

for i in range (0,n):
    if M[i][m-1] > maxim2:
        maxim2 = M[i][m-1]
k = 0
for i in range (0,n):
    if M[i][m-1] == maxim2:
        k += 1



for i in M:
    print(i)
print(maxim2)

if k == 1:
    print("Drum unic")
else:
    print("Drumul nu este unic")


