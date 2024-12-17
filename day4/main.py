def getCount():
  puzzle = []
  horizCount = 0
  with open('day4/input.txt', 'r') as file:
      for line in file:
        horizCount += line.count('XMAS') + line.count('SAMX')
        row = []
        for c in line.strip():
           row += c
        puzzle.append(row)
  return horizCount + getOtherCounts(puzzle)

def getXCount():
  puzzle = []
  with open('day4/input.txt', 'r') as file:
      for line in file:
        row = []
        for c in line.strip():
           row += c
        puzzle.append(row)
  return getXCountHelper(puzzle)

def getValidCount(s):
  return int(s == 'XMAS' or s == 'SAMX')

def isValidX(s):
  return s == 'MS' or s == 'SM'

def getOtherCounts(p):
  numRows = len(p)
  numCols = len(p[0])
  count = 0
  for i in range(0, numRows):
    for j in range(0, numCols):
      count += getCountForIndex(p, i, j, numRows, numCols)
  return count

def getCountForIndex(p,i,j, numRows, numCols):
  if p[i][j] != 'X': return 0
  WORD_LEN = 4
  dirs = {'up': '', 'down': '', 'ne':'', 'se': '', 'sw': '', 'nw': ''}
  for k in range(0, WORD_LEN): 
    dirs['up'] += p[i-k][j] if i-k >= 0 else ''
    dirs['down'] += p[i+k][j] if i+k < numRows else ''
    dirs['se'] += p[i+k][j+k] if i+k < numRows and j+k < numCols else ''
    dirs['nw'] += p[i-k][j-k] if i-k >= 0 and j-k >= 0 else '' 
    dirs['sw'] += p[i+k][j-k] if i+k < numRows and j-k >= 0 else ''
    dirs['ne'] += p[i-k][j+k] if i-k >= 0 and j+k < numCols else '' 
  return sum([getValidCount(v) for v in dirs.values()])

def getXCountHelper(p):
  numRows = len(p)
  numCols = len(p[0])
  count = 0
  for i in range(0, numRows):
    for j in range(0, numCols):
      count += getXCountForIndex(p, i, j)
  return count

def getXCountForIndex(p,i,j):
  if p[i][j] != 'A': return 0
  if i-1<0 or j-1<0: return 0
  if i+1>=len(p) or j+1>=len(p): return 0
  se = p[i+1][j+1]; nw = p[i-1][j-1]
  ne = p[i-1][j+1]; sw = p[i+1][j-1]
  return int(isValidX(se+nw) and isValidX(ne+sw))

def main():
  print(getCount()) # 2562
  print(getXCount()) # 1902

main()