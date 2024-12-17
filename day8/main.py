from itertools import combinations

def getMappedArea():
  area = []
  nodes = {}
  with open('day8/input.txt', 'r') as file:
    i = 0
    for line in file:
      row = []
      for j, c in enumerate(line.strip()):
        row.append(c)
        if c != '.': nodes.setdefault(c, []).append((i,j))
      area.append(row)
      i+=1
  return area, nodes

def getNumAntinodes(area, nodes):
  antinodes = []
  for positions in nodes.values():
    antinodes += getAntinodes(area, positions)
  return len(set(antinodes))

def getNumAntinodesWithResonantHarmonics(area, nodes):
  antinodes = []
  for positions in nodes.values():
    if len(positions) > 1: antinodes += positions
    antinodes += getAntinodesWithResonantHarmonics(area, positions)
  return len(set(antinodes))

def getAntinodes(area, positions):
  antinodes = set()
  numRows = len(area); numCols = len(area[0]) 
  for (i1,j1),(i2,j2) in combinations(positions, 2):
    diffI = i1 - i2; diffJ = j1 - j2
    antinodes.add((i1 + diffI, j1 + diffJ))
    antinodes.add((i2 - diffI, j2 - diffJ))
  return [(i,j) for (i,j) in antinodes if 0 <= i < numRows and 0 <= j < numCols]

def getAntinodesWithResonantHarmonics(area, positions):
  antinodes = set()
  numRows, numCols = len(area), len(area[0]) 

  def update(ai, aj, diffI, diffJ, multiplier):
    i, j = ai + diffI * multiplier, aj + diffJ * multiplier
    while 0 <= i < numRows and 0 <= j < numCols:
      antinodes.add((i, j))
      multiplier += 1
      i, j = ai + diffI * multiplier, aj + diffJ * multiplier

  for (i1,j1),(i2,j2) in combinations(positions, 2):
    diffI = i1 - i2; diffJ = j1 - j2
    update(i1, j1, diffI, diffJ, 1)
    update(i2, j2, -diffI, -diffJ, 1)
  return antinodes 

def main():
  area, nodes = getMappedArea()
  print(getNumAntinodes(area, nodes)) #256
  print(getNumAntinodesWithResonantHarmonics(area,nodes)) #1005

main()