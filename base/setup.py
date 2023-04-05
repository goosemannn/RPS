import os
import sys

with open('./game.py', 'w') as f:
  with open('./base/game.py.txt', 'r') as f2:
    baseGame = f2.read()
    gameCode = baseGame.replace('%GAMEFOLDER%', sys.argv[2])
    f.write(gameCode)
    

