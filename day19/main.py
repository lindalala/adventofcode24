SEEN = {}

def getDesignsAndTowels():
  with open('day19/input.txt', 'r') as file:
    designs = []
    towels = []
    for line in file:
      parts = line.strip().split(',') 
      lenP = len(parts)
      if lenP > 1:
        towels = [p.strip() for p in parts]
      elif lenP == 1 and len(parts[0])>0:
        designs.append(parts[0].strip())
  return designs, set(towels)

def getCountDesigns():
  designs, towels = getDesignsAndTowels()
  maxT = max([len(t) for t in towels])
  count = 0
  for d in designs:
    isPos = isDesignPossible(d,towels, maxT)
    count += isPos
  return count

def getCountDesigns2():
  designs, towels = getDesignsAndTowels()
  maxT = max([len(t) for t in towels])
  return sum([getPossibleDesignsCount(d,towels, maxT) for d in designs])

def getPossibleDesignsCount(design,towels,maxT):
  if design == '': return 1
  if len(design) == 1: return int(design in towels)
  res = [0]
  for i in range(1,min(maxT+1,len(design)+1)):
    prefix = design[0:i]
    if prefix not in towels: continue
    rest = design[i:]
    if rest not in SEEN: 
      SEEN[rest] = getPossibleDesignsCount(rest,towels,maxT)
    res.append(SEEN[rest])
  return sum(res)

def isDesignPossible(design,towels,maxT):
  if design == '' or design in towels: return True
  for i in range(min(maxT+1,len(design))):
    if design[0:i] not in towels: continue
    rest = design[i:]
    if rest not in SEEN: 
      SEEN[rest] = isDesignPossible(rest,towels,maxT)
    if SEEN[rest]: return True
  return False

def main():
  # print(getCountDesigns()) #319
  print(getCountDesigns2()) #692575723305545
  
main()