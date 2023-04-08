import multiprocessing
import time 
import os

gameNumber = 0
bot1Base = """
import random
def choice():
  return random.choice(%LIST%)
"""
bot2Base = """
import random
def choice():
  return random.choice(%LIST%)
"""
gameBase = """
import threading
import json
import os
import games._%GAMEFOLDER%.bot1 as bot1 
import games._%GAMEFOLDER%.bot2 as bot2
def gameRun():
  with open('./games/_%GAMEFOLDER%/results.json', 'r') as f: results = json.load(f)
  for i in range(0, 1000000):
    bot1Choice = bot1.choice() 
    bot2Choice = bot2.choice() 
    winner = 0
    if bot1Choice == "r":
      if bot2Choice == 'p': winner = 2
      elif bot2Choice =='s': winner = 1
      else: winner = 0
    elif bot1Choice == "p":
      if bot2Choice == 'r': winner = 1
      elif bot2Choice == 's': winner = 2
      else: winner = 0
    elif bot1Choice == "s":
      if bot2Choice == "p": winner = 1
      elif bot2Choice == 'r': winner = 2
      else:winner = 0 
    results['total'] += 1
    if winner == 0: results['ties'] += 1
    elif winner == 1: results['bot1Wins'] += 1
    elif winner == 2: results['bot2Wins'] += 1
    with open('./games/_%GAMEFOLDER%/results.json', 'w') as f: f.write(json.dumps(results))
"""
setupBase = """
import os
import sys
import random
def setup(gameNumber):
  with open('./games/_'+str(gameNumber)+'/game.py', 'w') as f:
    with open('./base/game.py.txt', 'r') as f2:
      baseGame = f2.read()
      gameCode = baseGame.replace('%GAMEFOLDER%', gameNumber)
      f.write(gameCode)
  with open(f'./games/_{gameNumber}/bot1.py', 'w') as f:
    with open('./base/bot1.py.txt', 'r') as f2:
      rockList = ["r" for x in range(0, random.randint(1, 20))]
      paperList = ["p" for x in range(0, random.randint(1, 20))]
      scissorsList = ["s" for x in range(0, random.randint(1, 20))]
      l = rockList + paperList + scissorsList 
      baseSetup = f2.read()
      setupCode = baseSetup.replace('%LIST%', str(l))
      f.write(setupCode)
  with open(f'./games/_{gameNumber}/bot2.py', 'w') as f:
    with open('./base/bot2.py.txt', 'r') as f2:
      rockList = ["r" for x in range(0, random.randint(1, 20))]
      paperList = ["p" for x in range(0, random.randint(1, 20))]
      scissorsList = ["s" for x in range(0, random.randint(1, 20))]
      l = rockList + paperList + scissorsList 
      baseSetup = f2.read()
      setupCode = baseSetup.replace('%LIST%', str(l))
      f.write(setupCode)
  with open(f'./games/_{gameNumber}/results.json', 'w') as f:
    f.write('{"total": 0, "bot1Wins": 0, "bot2Wins": 0, "ties": 0}')
"""

def writeBases():
  os.mkdir('./base')
  os.mkdir('./func')
  os.mkdir('./games')
  with open('./base/bot1.py.txt', 'w') as f: f.write(bot1Base)
  with open('./base/bot2.py.txt', 'w') as f: f.write(bot2Base)
  with open('./base/game.py.txt', 'w') as f: f.write(gameBase)
  with open('./func/setup.py', 'w') as f: f.write(setupBase)

def createGame(gameNumber):
  os.mkdir('./games/_' + str(gameNumber))
  import func.setup as setup
  setup.setup(str(gameNumber))

def runGame(gameNumber):
  game = __import__(f'games._{gameNumber}.game', fromlist=['gameRun'])
  game.gameRun()

  
def main():
  global gameNumber
  writeBases()

  createGame(gameNumber)
  time.sleep(1)
  runGame(gameNumber)
  gameNumber += 1


if __name__ == '__main__':
  main()