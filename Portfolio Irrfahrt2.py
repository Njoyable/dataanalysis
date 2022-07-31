import random

#Aufgabe 2
x=0
y=0
counter = 0
location = [x,y]
def step(location):
    randomNr = random.random()
    #rechts
    if(randomNr<=0.25):
        location[0] += 1
    #links
    elif(randomNr<=0.5):
        location[0] -= 1
    #vorne
    elif(randomNr<=0.75):
        location[1] += 1
    #hinten
    else:
        location[1] -= 1
    return location

def walking(x,y,location):
    counter = 0
    for j in range(x):
        location[0] = 0
        location[1] = 0
        for i in range(y):
            location = step(location)
            if isBack(location):
                counter +=1               
                break          
    print(counter/10_000)

def isBack(location):
    if(location[0] == 0 and location[1]==0):
        return True

print('Die Rückkehrwahrscheinlichkeit innerhalb 10.000 Schritten beträgt:')
walking(10_000,10_000,location)

print('Die Rückkehrwahrscheinlichkeit innerhalb 10.000 Schritten beträgt:')
walking(10_000,100_000,location)

print('Die Rückkehrwahrscheinlichkeit innerhalb 10.000 Schritten beträgt:')
walking(10_000, 1_000_000, location)





