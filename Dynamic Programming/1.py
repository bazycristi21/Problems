Piese = [(1,8),(1,5),(5,3),(5,2),(4,8),(2,4),(2,3),(2,2),(8,5)]


back = [1 for x in range(len(Piese))]
next = [-1 for x in range(len(Piese))]

Sol = []

for i in range(-len(Piese)+2,1):
    for j in range(-i +1,len(Piese)):
        if Piese[-i][1] == Piese[j][0] and back[-i] <= back[j]:
            back[-i] = back[j] + 1
            next[-i] = j

print(back)
print(next)

k=0
first = 0
last = 0

biggest_line = 0
biggest_first = -1
ok = 0

for i in range(0,len(Piese)):
    if next[i] != -1:
        ok = 1
    if ok == 1:
        line = 0
        first = i
        while i != -1:
            i = next[i]
            line += 1
        if line > biggest_line:
            biggest_line = line
            biggest_first = first
        ok = 0
i = biggest_first

while i != -1:

    Sol.append((Piese[i][0],Piese[i][1]))
    i = next[i]

first = 0
first_option = Sol[0][1]
second_option = Sol[len(Sol)-1][0]

nr_piese = 0

for i in Sol:
    for j in Piese:
        if i == j:
            nr_piese += 1

print(Sol)
print(first,last)

