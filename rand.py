import random

for i in range(0,20):
    year = random.randint(2000,2019)
    aime = random.randrange(0,2)
    number = random.randint(17,25)
    if(aime >= 1):
        print("gimme AMC 10 " +str(year) + " A "+ str(number))
    else:
        print("gimme AMC 10 " +str(year) + " B "+ str(number))
    