import math

RULES_BEFORE = {}

def getMiddleSums(l):
  return sum([x[math.floor(len(x)/2)] for x in l])

def getUpdates():
  correctUpdates = []
  incorrectUpdates = []
  with open('day5/input.txt', 'r') as file:
      for line in file:
        if '|' in line: # rule
          a,b = line.strip().split('|')
          RULES_BEFORE.setdefault(int(a), []).append(int(b))
        else: # update
          if len(line.strip()) < 1: continue
          update = [int(x) for x in line.strip().split(',')]
          correctUpdates.append(update) if isValidUpdate(update) else incorrectUpdates.append(update)
  return (correctUpdates, incorrectUpdates)

def getFixedUpdates(incorrectUpdates):
  fixedUpdates = []
  for u in incorrectUpdates:
    fixedUpdates.append(fixUpdate(u))
  return fixedUpdates

def fixUpdate(update):
  before = {u:[r for r in RULES_BEFORE.get(u, []) if r in update] for u in update}
  fixed = []
  for i in range(len(update)):
    toPop = None
    for u in update:
      if len(before[u]) == 0:
        fixed.append(u)
        before = {up:[r for r in before[up] if r != u] for up in before.keys()}
        toPop = u
        break
    update.pop(update.index(u))
  fixed.reverse()
  return fixed

def isValidUpdate(update):
  for i, v in enumerate(update):
    for r in RULES_BEFORE.get(v, []):
      if r in update and update.index(r) < i: return False
  return True

def main():
  (correctUpdates, incorrectUpdates) = getUpdates()
  print(getMiddleSums(correctUpdates)) # 5509
  print(getMiddleSums(getFixedUpdates(incorrectUpdates))) # 4407
  
main()