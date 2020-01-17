import queue


class Object:
    def __init__(self,weight1,value1):
        self.weight = weight1
        self.value = value1
    def afis(self):
        print(self.weight,self.value)


class Node:
    def __init__(self,level,profit,bound,weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight


def myComp(a,b):
    return a.value / a.weight < b.value / b.weight


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if myComp(arr[i],arr[j]):
                swapPositions(arr,i,j)

def bound(u, n, W, Obj_arr):
    sort(Obj_arr)
    if u.weight >= W:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight
    while j < n and totweight + Obj_arr[j].weight <= W:
        totweight += Obj_arr[j].weight
        profit_bound += Obj_arr[j].value
        j += 1
    if j < n:
        profit_bound += W - totweight * Obj_arr[j].value / Obj_arr[j].weight
    return profit_bound

def knapsack(W, Obj_arr, n):

    Q = queue.Queue()
    u = Node(-1,0,0,0)
    v = Node(-1,0,0,0)
    Q.put(u)
    maxProfit = 0
    while Q.qsize():
        u = Q.get()
        if u.level == -1:
            v.level = 0
        if u.level == n-1:
            continue
        v.level = u.level + 1

        v.weight = u.weight + Obj_arr[v.level].weight
        v.profit = u.profit + Obj_arr[v.level].value
        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit
        v.bound = bound(v,n,W,Obj_arr)
        if v.bound > maxProfit:
            Q.put(v)
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v,n,W,Obj_arr)
        if v.bound > maxProfit:
            Q.put(v)
    return maxProfit

W = 10
Obj_arr = [ Object(2,40), Object(3.14,50), Object(1.98,100), Object(5,95), Object(3,30)]

n = len(Obj_arr)
print(knapsack(W,Obj_arr,n))
