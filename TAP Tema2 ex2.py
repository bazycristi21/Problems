import math

F1= open("F1.txt","r")

F2= open("F2.txt", "r")

dict1 ={}
dict2 ={}
i =1

for line in F1:
    for word in line.split():
        if word not in dict2:
            dict2[word]=0
        if word in dict1:

            dict1[word]+=1
        else:
            dict1[word]=1
        i+=1

i=1
for line in F2:
    for word in line.split():
        if word not in dict1:
            dict1[word] = 0
        if word in dict2:
            dict2[word]+=1
        else:
            dict2[word]=1
        i+=1
print(dict1)
print(dict2)
sum = 0.0
rad1 = 0.0
rad2 = 0.0
for i in dict1:
    print(dict1[i])
    print(dict2[i])
    sum=dict1[i]*dict2[i]+sum
    rad1= dict1[i]*dict1[i]+rad1
    rad2= dict2[i]*dict2[i]+rad2


rad=math.sqrt(rad1)*math.sqrt(rad2)

rez=sum/rad

print(rez)



