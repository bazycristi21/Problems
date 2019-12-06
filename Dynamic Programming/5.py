import numpy as np

L= [2,3,7,1,2,5,7,9,5]

start = 0
stop = len(L) - 1
user_pick = 0
pc_pick = 1
pc_sum = 0
user_sum = 0
M = [[0 for x in range(0,len(L))] for x in range(0,len(L))]
for i in range(0,len(L)-1):
    M[i][i+1] = max(L[i]-L[i+1],L[i+1]-L[i])
    M[i][i] = L[i]

for i in range(0,len(L)-1):
    for j in range(0,len(L)):
        M[i][j] = max(M[i][j],L[i]+L[j] - M[i+1][j-1])


print(M[1][len(L)-1])

while len(L) > 0:
    print(M[start][stop])
    r = np.random.randint(2)
    if r == 1:
        if pc_pick == 1:
            pc_sum += L[len(L)-1]
            pc_pick = 0
            user_pick = 1
        else:
            user_sum += L[len(L)-1]
            user_pick =0
            pc_pick = 1
        del L[len(L)-1]
        stop -= 1
    else:
        if pc_pick == 1:
            pc_sum += L[0]
            pc_pick =0
            user_pick = 0
        else:
            user_pick += L[0]
            pc_pick = 1
            user_pick = 0
        del L[0]
        start += 1

