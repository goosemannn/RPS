import threading
import json
import games.1.bot1 as bot1
import games.1.bot2 as bot2
def game():
  with open('./games/1/results.json', 'r') as f: results = json.load(f)
  for i in range(0, 10):
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
    with open('./games/%GAMEFOLDER/results.json', 'w') as f: f.write(json.dumps(results))