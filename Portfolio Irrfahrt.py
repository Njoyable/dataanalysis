import random

#Aufgabe 1

def step(x):
    randomNr = random.random()
    if (randomNr<=0.5):
        x = x+1
    else:
        x = x-1
    return x
        
def isBack(x):
    if(x == 0):
        return True

def walking(x,y,location):    
    counter =0
    for j in range(x):
        location = 0
        for i in range(y):
            location = step(location)
            if (isBack(location)):
                counter +=1            
                break          
    print(counter/10_000)

location = 0
#innerhalb 10_000 Schritte
print('Die Wahrscheinlichkeit, innerhalb von 10.000 Schritten wieder zurückzukommen beträgt:')
walking(10_000,10_0000,location)

#innerhalb 100_000 Schritte
print('Die Wahrscheinlichkeit, innerhalb von 100.000 Schritten wieder zurückzukommen beträgt:')
walking(10_000,100_000,location)

#innerhalb 1_000_000 Schritte
print('Die Wahrscheinlichkeit, innerhalb von 1.000.000 Schritten wieder zurückzukommen beträgt:')
walking(10_000,1_000_000,location)






    
    
    
    
    
    
    
    
    
    