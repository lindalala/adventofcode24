def getTrailheadScore():
  topoMap, trailheads = getTopoMapAndTrailheads()
  scores = []
  for th in trailheads:
    scores.append(len(getEndpointsForTrailhead(topoMap, th, [], 1)))
  return sum(scores)

def getTrailheadRating():
  topoMap, trailheads = getTopoMapAndTrailheads()
  scores = 0
  for th in trailheads:
    scores += getRatingsForTrailhead(topoMap, th, 1)
  return scores

def getTopoMapAndTrailheads():
  topoMap = []
  trailheads = []
  with open('day10/input.txt', 'r') as file:
    curI = 0
    for line in file:
      row = []
      for curJ, h in enumerate(line.strip()):
        if h == '.': h = -1
        height = int(h)
        row.append(height)
        if height == 0: trailheads.append((curI,curJ))
      topoMap.append(row)
      curI += 1
  return topoMap, trailheads

def getEndpointsForTrailhead(topoMap, trailhead, ends, nextHeight):
  (ti, tj) = trailhead 
  next = getNextSteps(topoMap, ti, tj)
  for (ni,nj) in next:
    if topoMap[ni][nj] == nextHeight:
      if nextHeight == 9:
        ends.append((ni,nj))
      else: ends = getEndpointsForTrailhead(topoMap, (ni,nj), ends, nextHeight+1)
  return list(set(ends))

def getRatingsForTrailhead(topoMap, trailhead, nextHeight):
  if nextHeight == 10: return 1
  (ti, tj) = trailhead 
  rating = 0
  for (ni,nj) in getNextSteps(topoMap, ti, tj):
    if topoMap[ni][nj] == nextHeight:
      rating += getRatingsForTrailhead(topoMap, (ni,nj), nextHeight+1)
  return rating

def getNextSteps(topoMap, i, j):
  next = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
  return [(i,j) for (i,j) in next if 0<=i<len(topoMap) and 0<=j<len(topoMap[0])]

def main():
  # print(getTrailheadScore()) #459
  print(getTrailheadRating()) #459

main()