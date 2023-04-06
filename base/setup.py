import os
import sys
import random


#os.mkdir('./games/' + sys.argv[1])

print(os.listdir('./'))
with open('./games/'+str(sys.argv[1])+'/game.py', 'w') as f:
  with open('./base/game.py.txt', 'r') as f2:
    baseGame = f2.read()
    gameCode = baseGame.replace('%GAMEFOLDER%', sys.argv[1])
    f.write(gameCode)

with open(f'./games/{sys.argv[1]}/bot1.py', 'w') as f:
  with open('./base/bot1.py.txt', 'r') as f2:
    rockList = ["r" for x in range(0, random.randint(1, 20))]
    paperList = ["p" for x in range(0, random.randint(1, 20))]
    scissorsList = ["s" for x in range(0, random.randint(1, 20))]
    l = rockList + paperList + scissorsList 
    baseSetup = f2.read()
    setupCode = baseSetup.replace('%LIST%', str(l))
    f.write(setupCode)

with open(f'./games/{sys.argv[1]}/bot2.py', 'w') as f:
  with open('./base/bot2.py.txt', 'r') as f2:
    rockList = ["r" for x in range(0, random.randint(1, 20))]
    paperList = ["p" for x in range(0, random.randint(1, 20))]
    scissorsList = ["s" for x in range(0, random.randint(1, 20))]
    l = rockList + paperList + scissorsList 
    baseSetup = f2.read()
    setupCode = baseSetup.replace('%LIST%', str(l))
    f.write(setupCode)
    

