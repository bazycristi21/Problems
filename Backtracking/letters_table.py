n = 4
m = 4

Mat = [
    ["A","B","A","E"],
    ["C","E","D","W"],
    ["A","G","H","J"],
    ["C","A","D","Y"]
]
vect = {"A":0,
        "C":0,
        "B":0,
        "E":0,
        "D":0,
        "W":0,
        "J":0,
        "Y":0,
        "H":0,
        "G":0}

OK = 1
maxim = 1
road = []
All_roads = []


def recursion(x,y,vect,length, road):
    global maxim
    global All_roads
    vect[Mat[x][y]] = True
    road.append(Mat[x][y])
    OK = 1
    if x == 0 and y == 0 :
        recursion(x+1,y,vect,1,road)
        recursion(x,y+1,vect,1,road)
    else:
        if x > 0:
            if vect[Mat[x-1][y]] != True:
                recursion(x-1,y,vect,length+1,road)
                OK = 0
        if y > 0:
            if vect[Mat[x][y-1]] != True:
                recursion(x,y-1,vect,length+1,road)
                OK = 0
    if x < n-1:
            if vect[Mat[x+1][y]] != True:
                recursion(x+1,y,vect,length+1,road)
                OK = 0
    if y < n-1:
            if vect[Mat[x][y+1]] != True:
                recursion(x,y+1,vect,length+1,road)
                OK = 0
    if OK == 1:
        if length > maxim:
            maxim = length
            road_copy = road.copy()
            All_roads.append(road_copy)
    vect[road[len(road) - 1]] = False
    road.pop(len(road)-1)

recursion(0,0,vect,0,road)


print(maxim)
for i in All_roads:
    if len(i)-1 == maxim:
        print(i)
