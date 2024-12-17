SEEN = set()

def getPrice():
  regions = getRegions()
  rows, cols = len(regions), len(regions[0])
  price = 0
  for i in range(len(regions)):
    for j in range(len(regions[0])):
      if (i,j) not in SEEN: 
        price += getPriceHelper(regions, i, j, rows, cols)
  return price


def getPriceHelper(regions, i, j, rows, cols):
  region = regions[i][j]
  perimeter = []
  perims = {}
  area = 0
  nexts = [(i,j)]
  while len(nexts) > 0:
    (nI,nJ) = nexts.pop()
    if (nI,nJ) in SEEN: continue
    neighbors = getNextsWithDirection(nI,nJ)
    area += 1
    for (x,y,dir) in neighbors:
      if not(0<=x<rows and 0<=y<cols) or regions[x][y] != region: 
        perimeter.append((x,y))
        perims.setdefault(dir,[]).append((x,y))
      else: 
        if (x,y) not in SEEN: nexts.append((x,y))
    SEEN.add((nI,nJ))

  sides = 0
  for ps in perims.values():
    perimX = {}; perimY = {}
    for (x,y) in ps:
      perimX.setdefault(x, []).append(y)
      perimY.setdefault(y, []).append(x)
  
    for x,ys in perimX.items():
      ys = sorted(ys)
      cur = ys.pop(0)
      curs = [cur]
      while len(ys) > 0:
        if cur+1 in ys: 
          curs.append(cur+1)
          ys.remove(cur+1)
          cur = cur+1
        else: 
          if len(curs) > 1:
            sides += 1
            for y in curs:
              perimeter.remove((x,y))
          cur = ys.pop(0)
          curs = [cur]
      if len(curs)>1: 
        sides += 1
        for y in curs: perimeter.remove((x,y))

    for y,xs in perimY.items():
      xs = sorted(xs)
      cur = xs.pop(0)
      curs = [cur]
      while len(xs) > 0:
        if cur+1 in xs: 
          curs.append(cur+1)
          xs.remove(cur+1)
          cur = cur+1
        else: 
          if len(curs) > 1:
            sides += 1
            for x in curs:
              if (x,y) in perimeter: perimeter.remove((x,y))
          cur = xs.pop(0)
          curs = [cur]
      if len(curs)>1: 
        sides += 1
        for x in curs: 
          if (x,y) in perimeter: perimeter.remove((x,y))

  return area * (sides + len(perimeter))

def getPriceHelperP1(regions, i, j, rows, cols):
  region = regions[i][j]
  perimeter = 0
  area = 0
  nexts = [(i,j)]
  while len(nexts) > 0:
    (nI,nJ) = nexts.pop()
    if (nI,nJ) in SEEN: continue
    neighbors = getNexts(nI,nJ)
    area += 1
    SEEN.add((nI,nJ))
    for (x,y) in neighbors:
      if not(0<=x<rows and 0<=y<cols) or regions[x][y] != region: 
        perimeter += 1
      else: 
        if (x,y) not in SEEN: nexts.append((x,y))
  return area * perimeter

def getNexts(i,j):
  return [(i-1,j), (i+1, j), (i, j+1), (i, j-1)]

def getNextsWithDirection(i,j):
  return [(i-1,j, 'S'), (i+1, j, 'N'), (i, j+1, 'E'), (i, j-1, 'W')]

def getRegions():
  regions = []
  with open('day12/input.txt', 'r') as file:
    for line in file:
      row = []
      for curJ, region in enumerate(line.strip()):
        row.append(region)
      regions.append(row)
  return regions

def main():
  # print(getPrice()) # 1415378 P1
  print(getPrice()) # 862714

main()