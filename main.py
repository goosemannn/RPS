import multiprocessing 

def writeBases():
  pass

def writeData():
  pass

def createGamesFolder():
  pass

def setup():
  pass

def runFirstGame():
  pass 
  
def main():
  pass

game = __import__('base.game')
p = multiprocessing.Process(target=game.game)
p.start()
p.join()