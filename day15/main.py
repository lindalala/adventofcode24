UP,DOWN,LEFT,RIGHT = '^','v','<','>'
BOX,ROBOT,EMPTY,WALL,LBOX,RBOX = 'O','@','.','#','[',']'

def readInput():
  grid = []
  dirs = []
  start = None
  dirOptions = set([UP,DOWN,LEFT,RIGHT])
  gridOptions = set([BOX,EMPTY,ROBOT,WALL])
  with open('day15/testinput.txt', 'r') as file:
    i,j = 0,0
    for line in file:
      row = []
      for j, c in enumerate(line):
        if c in dirOptions:
          dirs.append(c)
          continue
        if c == ROBOT: start = (i,j)
        if c in gridOptions: row += c
      i+=1
      if len(row)>0: grid.append(row)
  return grid,dirs,start

def readInputScaled():
  grid = []
  dirs = []
  start = None
  dirOptions = set([UP,DOWN,LEFT,RIGHT])
  with open('day15/input.txt', 'r') as file:
    for line in file:
      row = []
      for c in line:
        if c in dirOptions:
          dirs.append(c)
          continue
        if c == ROBOT: 
          row += [ROBOT,EMPTY]
        elif c == BOX:
          row += [LBOX,RBOX]
        elif c == EMPTY or c == WALL:
          row += c*2
      if len(row)>0: grid.append(row)
  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      if col == ROBOT: start = (i,j)
  return grid,dirs,start

def getFinalSumScaled(grid,dirs,start):
  res = 0
  for dir in dirs:
    grid,start = getNextGridScaled(grid,dir,start)
  for i, row in enumerate(grid):
    for j,col in enumerate(row):
      if grid[i][j] == LBOX: res += 100*i+j
  return res

def getFinalSum(grid,dirs,start):
  res = 0
  for dir in dirs:
    grid,start = getNextGrid(grid,dir,start)
  for i, row in enumerate(grid):
    for j,col in enumerate(row):
      if grid[i][j] == BOX: res += 100*i+j
  return res

def getNextGrid(grid,dir,start):
  startX,startY = start
  (i,j) = getNextPos(start, dir)
  if not isInBounds(grid,(i,j)):
    return grid,start
  if grid[i][j] == EMPTY:
    grid[startX][startY] = EMPTY
    grid[i][j] = ROBOT
    return grid,(i,j)
  if grid[i][j] == BOX:
    (nI,nJ) = getNextPos((i,j), dir)
    while isInBounds(grid,(nI,nJ)) and grid[nI][nJ] != EMPTY:
      (nI,nJ) = getNextPos((nI,nJ),dir)
    if isInBounds(grid,(nI,nJ)): 
      grid[startX][startY] = EMPTY
      grid[i][j] = ROBOT
      grid[nI][nJ] = BOX
      return grid, (i,j)
    return grid,start
  print('unknown  grid item: ', grid[i][j])
  return grid,start

def getNextGridScaled(grid,dir,start):
  startX,startY = start
  (i,j) = getNextPos(start, dir)
  if not isInBounds(grid,(i,j)):
    return grid,start
  if grid[i][j] == EMPTY:
    grid[startX][startY] = EMPTY
    grid[i][j] = ROBOT
    return grid,(i,j)
  if grid[i][j] == LBOX or grid[i][j] == RBOX:
    (nI,nJ) = getNextPos((i,j), dir)
    isLBox = grid[i][j] == LBOX
    if dir == LEFT or dir == RIGHT:
      while isInBounds(grid,(nI,nJ)) and grid[nI][nJ] != EMPTY:
        (nI,nJ) = getNextPos((nI,nJ),dir)
      if isInBounds(grid,(nI,nJ)):
        grid[startX][startY] = EMPTY
        grid[i][j] = ROBOT
        useRbox = isLBox
        while nJ is not j:
          grid[nI][nJ] = RBOX if useRbox else LBOX
          useRbox = not useRbox
          nJ += 1 if nJ < j else -1
        return grid, (i,j)
      return grid,start
    if dir == UP or dir == DOWN:
      updates={}; seen = set(); empties=set(); nexts = [(i,j)]
      isLbox = grid[i][j] == LBOX
      otherBox = (i,j+1) if isLbox else (i,j-1)
      updates[otherBox] = EMPTY
      nexts.append(otherBox)
      while len(nexts)>0:
        (curI,curJ) = nexts.pop()
        if ((curI,curJ) in seen): continue
        seen.add((curI,curJ))
        (nI,nJ) = getNextPos((curI,curJ),dir)
        if not isInBounds(grid, (nI,nJ)): return grid,start
        updates[(nI,nJ)] = grid[curI][curJ] 
        empties.add((curI, curJ))
        if grid[nI][nJ] == LBOX: nexts += [(nI,nJ), (nI,nJ+1)]
        elif grid[nI][nJ] == RBOX: nexts += [(nI,nJ), (nI,nJ-1)]
      for (x,y) in empties:
        if (x,y) not in updates: grid[x][y] = EMPTY
      for (x,y),v in updates.items():
        grid[x][y] = v
      grid[startX][startY] = EMPTY
      grid[i][j] = ROBOT
      return grid,(i,j)
  print('unknown  grid item: ', grid[i][j])
  return grid,start

def isInBounds(grid,coord):
  i,j = coord
  return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] is not WALL

def getNextPos(coord,dir):
  (i,j) = coord
  if dir == UP: return (i-1,j)
  if dir == DOWN: return (i+1,j)
  if dir == LEFT: return (i,j-1)
  if dir == RIGHT: return (i,j+1)
  print('unknown  dir')
  return None

def printGrid(grid):
  for i,row in enumerate(grid): 
    print(str(i)+ ': '+''.join(row))

def main():
  print(getFinalSumScaled(*readInputScaled())) # 1521952
  # print(getFinalSum(*readInput())) # 1487337
  
main()