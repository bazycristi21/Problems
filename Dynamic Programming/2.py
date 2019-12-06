M = [
    [3,8,4,3],
    [2,4,2,6],
    [1,7,11,5],
]
M_copy =  [
    [3,8,4,3],
    [2,4,2,6],
    [1,7,11,5],
]

n = len(M)
m = len(M[0])

for j in range(1, m):

    for i in range(0,n):
        maxim = 0
        if i == 0:
            maxim = max(M[i][j-1],M[i+1][j-1])
        elif i == n-1:
            maxim = max(M[i][j-1],M[i-1][j-1])
        if i != 0 and i != n-1:
            maxim = max(M[i][j-1],M[i-1][j-1],M[i+1][j-1])
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



k = -1
for i in range(0,len(M)):
    if M[len(M)-1][i] == maxim2:
        k = i

Drum = []

def ref_drum(i , j):
            if j == -1:
                return
            if i == 0:
                maxim = max(M[i][j-1],M[i+1][j-1])

            elif i == n-1:
                maxim = max(M[i][j-1],M[i-1][j-1])
            if i != 0 and i != n-1:
                maxim = max(M[i][j-1],M[i-1][j-1],M[i+1][j-1])
            for k in range(0,len(M)):
                if maxim == M[k][j-1]:
                    i = k
                    j = j-1
            Drum.append(M_copy[i][j])
            ref_drum(i,j)

ref_drum(k,len(M[0])-1)
Drum.reverse()
Drum.append(Drum[0])
del Drum[0]
print(Drum)
