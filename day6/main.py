N = 0; E = 1; S = 2; W = 3

def getMappedArea():
  area = []
  with open('day6/input.txt', 'r') as file:
    for line in file:
      row = []
      for c in line.strip():
        row.append(c)
      area.append(row)
  return area

def getVisitedPositionsCount(area):
  visited = set()
  numRows = len(area); numCols = len(area[0])
  curI, curJ = getStartingPos(area); curDir = N
  while 0 <= curI < numRows and 0 <= curJ < numCols:
    visited.add((curI,curJ))
    nextI, nextJ, nextDir = getNextValidPos(area, curI, curJ, curDir)
    curI, curJ, curDir = nextI, nextJ, nextDir
  return len(visited)

def getObstaclesCount(area):
  obstaclesCount = 0
  numRows = len(area); numCols = len(area[0])
  startI, startJ = getStartingPos(area)
  curI, curJ = startI, startJ; curDir = N
  for (r, c) in [(r, c) for r in range(numRows) for c in range(numCols)]:
    if (r,c) == getStartingPos(area) or area[r][c] == '#':
      continue
    if doesGuardLoop(area, r, c): obstaclesCount += 1 
  return obstaclesCount

def doesGuardLoop(area, r, c):
  visited = set()
  numRows = len(area); numCols = len(area[0])
  curI, curJ = getStartingPos(area); curDir = N
  while 0 <= curI < numRows and 0 <= curJ < numCols:
    if (curI,curJ,curDir) in visited: return True
    visited.add((curI,curJ, curDir))
    curI, curJ, curDir = getNextValidPos(area, curI, curJ, curDir, r, c)
  return False

def getNextPos(i, j, dir):
  newI = i; newJ = j
  if dir == N: newI -= 1   
  elif dir == E: newJ += 1 
  elif dir == S: newI += 1 
  else: newJ -= 1   
  return newI, newJ

def getNextValidPos(area, i, j, dir, newObstacleI=None, newObstacleJ=None):
  newI, newJ = getNextPos(i,j,dir); newDir = dir
  numRows = len(area); numCols = len(area[0])

  while  0 <= newI < numRows and 0 <= newJ < numCols and (area[newI][newJ] == '#' \
         or (newI == newObstacleI and newJ == newObstacleJ)):
    newDir = (newDir+1) % 4
    newI, newJ = getNextPos(i,j,newDir)
  return (newI, newJ, newDir)

def getStartingPos(area):
  return next(
    ((r, c) for r, row in enumerate(area) for c, pos in enumerate(row) if pos == '^'), 
    None
  )

def main():
  area = getMappedArea()
  print(getVisitedPositionsCount(area)) #5080
  print(getObstaclesCount(area)) #1919
  
main()