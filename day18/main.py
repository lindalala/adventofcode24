import heapq
EMPTY, WALL = '.','#'

def getGrid(size=70, bytes=1024):
   grid = [[EMPTY for _ in range(size+1)] for _ in range(size+1)]
   with open('day18/input.txt', 'r') as file:
    count = 0
    for line in file:
      if (count==bytes): break
      parts = line.strip().split(',')
      j,i = int(parts[0]),int(parts[1])
      grid[i][j] = WALL
      count += 1
    # for row in grid: print(''.join(row))
    return grid

def getNumBytes():
  with open('day18/input.txt', 'r') as file:
    count = 0
    for line in file:
      if len(line.strip().split(','))==2: count += 1
  return count

def getShortestPath(grid,start,end):
  pq = []  
  heapq.heappush(pq, (0, start)) 
  seen = set()
  while len(pq)>0:
    score,cur = heapq.heappop(pq)
    if cur in seen: continue
    seen.add(cur)
    if cur == end: return score
    nexts = [n for n in getNexts(cur) if n not in seen and isInBounds(grid,n)]
    for next in nexts:
      heapq.heappush(pq, (score+1,next))
  return None

def getPart2(size,start,end):
  low,high = 12, getNumBytes()
  row = None
  while low <= high:
    mid = (low + high) // 2
    isMidPossible = getShortestPath(getGrid(size=size,bytes=mid),start,end) is not None
    if isMidPossible and getShortestPath(getGrid(size=size,bytes=mid+1),start,end) is None:
      row = mid
      break
    elif isMidPossible:
      low = mid
    else:  
      high = mid

  with open('day18/input.txt', 'r') as file:
    count = 0
    for line in file:
      if count == row: 
        parts = line.strip().split(',')
        res = int(parts[0]),int(parts[1])
      count += 1
  return res
    
def getNexts(coord):
  (i,j) = coord
  return [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]

def isInBounds(grid,coord):
  i,j = coord
  return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] is not WALL

def main():
  # print(getShortestPath(getGrid(size=6, bytes=12),(0,0),(6,6)))
  # print(getShortestPath(getGrid(size=70),(0,0),(70,70))) #354
  # print(getPart2(6,(0,0),(6,6)))
  print(getPart2(70,(0,0),(70,70))) #(36, 17)

main()