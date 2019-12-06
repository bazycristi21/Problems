C = "aaacaaba"


Matrix = [[0 for x in range(len(C))] for y in range(len(C))]

for i in range(0,len(C)-1):
    Matrix[i][i] = 1
    if C[i] == C[i+1]:
        Matrix[i][i+1] = 1
Matrix[len(C)-1][len(C)-1] = 1

for k in range(0, len(C)):
    for i in range(1,len(C)-k-1):
        if Matrix[i][i+k] == 1:
            if C[i+k+1] == C[i-1]:
                Matrix[i-1][i+k+1] = 1

nr = 0
for i in Matrix:
    for j in i:
        if j == 1:
            nr += 1

for i in Matrix:
    print(i)
print(nr)

n = len(C)
Nr = [0 for x in range(n+2)]

Nr[n+1] = 0
Nr[n] = 1

nrMinimPalindrom = 0

for i in range(-n+1,0):
    nrMinimPalindrom = n + 2
    for k in range(-i+1,n+2):
         if Matrix[-i-1][k-2] == 1:
             if Nr[k] < nrMinimPalindrom:
                 nrMinimPalindrom = Nr[k]
    Nr[-i] = 1 + nrMinimPalindrom

counter = int(0)
lastPos = len(C)
newWord = ""
sol = []


while counter != Nr[1]:
    for i in range(0, len(Nr) - 1):
        if Nr[i] == counter + 1:
            counter += 1
            startPos = i - 1
            break

    for i in range(startPos, lastPos):
        newWord += C[i]

    sol.append(newWord)
    newWord = ""
    lastPos = startPos

sol.reverse()
print(sol)
print(Nr[1])

