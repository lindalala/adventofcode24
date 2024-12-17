import heapq
START,END,WALL,EMPTY = 'S','E','#','.'
N,E,S,W = 0,1,2,3

def getGridAndStart():
  start = None
  grid = []
  with open('day16/input.txt', 'r') as file:
    i=0
    for line in file:
      row = []
      for j, c in enumerate(line.strip()):
        if c == 'S':
          start=(i,j)
        row.append(c)
      grid.append(row)
      i+=1
    return grid, start, E

def getMinScore(grid,start,dir):
  pq = []  
  heapq.heappush(pq, (0, start,dir))  # (score, (x,y), dir)
  scores = {(start,dir):0}
  while len(pq)>0:
    score,cur,curDir = heapq.heappop(pq)
    (curX,curY) = cur
    if grid[curX][curY] == END: 
      return score
    nexts = getNexts(grid,cur,curDir)
    for (next,nextDir,nextWeight) in nexts:
      nextScore = score + nextWeight
      if (next,nextDir) not in scores or nextScore < scores[(next,nextDir)]:
        scores[(next,nextDir)] = nextScore
        heapq.heappush(pq, (nextScore,next,nextDir))
  return None

def isInBounds(grid,coord):
  i,j = coord
  return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] is not WALL

# returns list of (next,nextDir,weight)
def getNexts(grid,start,dir): 
  nexts = []
  for rotation in [0,-1,1]: 
    nextDir = (dir+rotation)%4
    next = getNextPos(start,nextDir)
    if isInBounds(grid,next): nexts.append((next,nextDir,1+1000*abs(rotation)))
  return nexts

def getNextPos(coord,dir):
  (i,j) = coord
  if dir == N: return (i+1,j)
  if dir == E: return (i,j+1)
  if dir == S: return (i-1,j)
  if dir == W: return (i,j-1)
  print('unknown  dir')
  return None

def getBestSeats(grid,start,dir):
  minScore = getMinScore(grid,start,dir)
  pq = []  
  heapq.heappush(pq, (0, start,dir,[start]))  # (score, (x,y), dir, path)
  scores = {(start,dir):0}
  seats = set()
  while len(pq)>0:
    score,cur,curDir,path = heapq.heappop(pq)
    (curX,curY) = cur
    if grid[curX][curY] == END: 
      seats.add(cur)
      if score==minScore:
        seats.update(path)
    nexts = getNexts(grid,cur,curDir)
    for (next,nextDir,nextWeight) in nexts:
      nextScore = score + nextWeight
      if (next,nextDir) not in scores or nextScore <= scores[(next,nextDir)]:
        scores[(next,nextDir)] = nextScore
        heapq.heappush(pq, (nextScore,next,nextDir,path+[cur]))
  return len(seats)

def main():
  #print(getMinScore(*getGridAndStart())) #133584
  print(getBestSeats(*getGridAndStart())) #622

main()