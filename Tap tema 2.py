import random

def stanga():
    #print("S",S[0])
    del S[0]

def dreapta():
    #print("D",S[len(S)-1])
    del S[len(S)-1]
i=0
flag=0
while i<10:
    i+=1
    S=[]

    firstpick = 0
    secondpick = 0
    size = random.randint(1,50)*2
    for _ in range (0,size):
        S.append(random.randint(1,100))

while len(S) > 0:
    if len(S)==2:
        if S[0]>S[1]:
            firstpick += S[0]
            stanga()
            secondpick += S[0]
            dreapta()
        else:
            firstpick +=S[1]
            dreapta()
            secondpick +=S[0]
            stanga()

    else:
        if S[0]-max(S[1],S[len(S)-1]) > S[len(S)-1]-max(S[0],S[len(S)-2]):
            firstpick += S[0]
            stanga()
        else:
            firstpick  +=  S[len(S) - 1]
            dreapta()
        rnd=random.randint(0,1)
        if rnd==0 :
            secondpick += S[0]
            stanga()
        if rnd==1:
            secondpick += S[len(S)-1]
            dreapta()
if firstpick < secondpick:
    flag=1
    print("That's not good")




