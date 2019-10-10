Par=[(10,2,31),(8,50,60),(7,50,60)]

maxim=0
Par=sorted(Par)
for i in range (0,len(Par)):
    Par[i]=sorted(Par[i])
print(Par)
for pereche in Par:
    if(min(pereche[0],pereche[1],pereche[2])>maxim):
        maxim=min(pereche[0],pereche[1],pereche[2])

dict ={}

for pereche in Par:
    a=(pereche[0],pereche[1])
    if(a in dict):
        if(min(a[1],a[0],dict[a]+pereche[2])>maxim):
            maxim=min(a[1],a[2],dict[a]+pereche[2])
        if (dict[a] < pereche[2]):
            dict[a] = pereche[2]
    else:
        dict[a]=pereche[2]
    b=(pereche[1],pereche[2])
    if (b in dict):
        if (min(b[1], b[0], dict[b] + pereche[0]) > maxim):
            maxim = min(b[1], b[0], dict[b] + pereche[0])
        if (dict[b] < pereche[0]):
            dict[b] = pereche[0]
    else:
        dict[b] = pereche[0]
    c=(pereche[0],pereche[2])
    if (c in dict):
        if (min(c[1], c[0], dict[c] + pereche[1]) > maxim):
            maxim = min(c[1], c[0], dict[c] + pereche[1])
        if (dict[c] < pereche[1]):
            dict[c] = pereche[1]
    else:
        dict[c] = pereche[1]
print(maxim)


