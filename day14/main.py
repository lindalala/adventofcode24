import math
import re
import os
import json
WIDTH = 101
HEIGHT = 103
WIDTH_TEST = 11
HEIGHT_TEST = 7

def getSafetyFactor(seconds=100):
  midX,midY = WIDTH//2, HEIGHT//2
  quadCounts = [0]*4
  for (x,y) in getPositions(seconds):
    if x!=midX and y!=midY: 
      if x<midX and y<midY: quadCounts[0]+=1
      elif x>midX and y<midY: quadCounts[1]+=1
      elif x>midX and y>midY: quadCounts[2]+=1
      else: quadCounts[3]+=1
  return math.prod(quadCounts)

def getPositions(seconds):
  pos = []
  with open('day14/input.txt', 'r') as file:
    res = {}
    for line in file:
      matches = re.findall(r'[-]?\d+,\s*[-]?\d+', line)
      (startX,startY), (vX,vY) = (tuple(map(int, pair.split(','))) for pair in matches)
      pos.append(getPositionAfterXSeconds(startX, startY, vX, vY, seconds))
  return pos

def getPositionAfterXSeconds(startX,startY,velocityX,velocityY,secs):
  return ((startX+secs*velocityX)%WIDTH, (startY+secs*velocityY)%HEIGHT)

def writeStartPositions():
  pos = []
  with open('day14/input.txt', 'r') as file:
    coords = []
    for line in file:
      matches = re.findall(r'[-]?\d+,\s*[-]?\d+', line)
      (startX,startY), (vX,vY) = (tuple(map(int, pair.split(','))) for pair in matches)
      # Structure the data in the desired format
      data = {
        'x': startX,
        'y': startY,
        'vX': vX,
        'vY': vY
      }
      coords.append(data)
  # Write to a file
  with open('day14/starts.json', 'w') as file:
    json.dump(coords, file)  # Write JSON data in the desired format
  return pos

def getRepeatStep():
  posDict = {}
  for i in range(100000):
    pos = set(getPositions(i))
    if pos in posDict.values():
      print(i)
      return
    posDict[i] = pos

def writeToFile():
  res = {}
  for i in range(10000):
    pos = getPositions(i)
    if hasDiagonals(pos):
      res[i] = getGrid(pos)

  with open('day14/output.txt', 'w') as file:
    for step, grid in res.items():
      file.write('Grid for Step ' + str(step)+'\n')
      for row in grid:
        file.write(''.join(map(str, row)) + '\n')
    file.write('\n')

def hasDiagonals(pos):
  count = 0
  for (x,y) in pos:
    if (x+1, y+1) in pos or (x-1,y-1) in pos or (x+1, y-1) in pos or (x-1, y+1) in pos:
      count += 1
  return count > 200

def getGrid(pos):
  res = []
  for i in range(HEIGHT):
    row = []
    for j in range(WIDTH):
      row.append('X' if (j,i) in pos else '.')
    res.append(row)
  return res
  

def main():
  # print(getSafetyFactor()) #221142636
  # writeStartPositions()
  # print(getRepeatStep())
  writeToFile()

main()