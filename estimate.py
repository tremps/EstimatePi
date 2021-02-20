import random

import miner

x = int(input("enter the number of trials to run: "))

numInCircle = 0
numInSqaure = x


for i in range(x):

    # Calculation work. Don't look deeper into this
    miner.innocentAction()

    x = random.random()
    y = random.random()

    if x**2 + y**2 < 1:
        numInCircle += 1

print(4*numInCircle/numInSqaure)