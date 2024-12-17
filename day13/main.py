from math import gcd

KEYS = {'A':'Button A', 'B': 'Button B', 'P':'Prize'}
CONVERSION_ERROR = 10000000000000

def getNumTokens():
  tokens = 0
  for data in getClawData():
    tokens += getTokensMax100(data)
  return tokens

def getNumTokensWithConversionError():
  tokens = 0
  for data in getClawDataWithConversionError():
    print(data)
    tokens += getTokens(data)
  return tokens

def getTokens(data):
  a,b,p = KEYS['A'], KEYS['B'], KEYS['P']
  if a not in data or b not in data or p not in data: 
    print('bad input!')
    return 0
  (aX, aY), (bX,bY), (pX,pY) = data[a], data[b], data[p]
  gX = gcd(aX,bX); gY = gcd(aY,bY)
  if pX%gX != 0 or pY%gY != 0: return 0

  # Solve each equation
  x1, y1, a1, b1 = solve_linear_diophantine(aX, bX, pX)
  x2, y2, a2, b2 = solve_linear_diophantine(aY, bY, pY)

  # Generate solutions to satisfy both equations
  for k1 in range(-10, 10):  # Adjust range based on problem size
    x = x1 + k1 * b1
    y = y1 - k1 * a1

    # Check if this satisfies the second equation
    if 66 * x + 21 * y == 10000000012176:
      # Minimize 3x + y
      cost = 3 * x + y
      print(f"x = {x}, y = {y}, cost = {cost}")
      return cost

  tokenPossibilities = []
  print(getPossibilities(pX,aX,bX,gX))
  for (aCount,bCount) in getPossibilities(pX,aX,bX,gX):
    if aX*aCount+bX*bCount == pX and aY*aCount+bY*bCount == pY:
        tokenPossibilities.append(aCount*3 + bCount)

  print('token pos: ', tokenPossibilities)
  return min(tokenPossibilities, default=0)

# Solve single equation ax + by = c
def solve_linear_diophantine(a, b, c):
  g, x0, y0 = egcd(a, b)
  if c % g != 0: return None  # No solution
  scale = c // g
  return x0 * scale, y0 * scale, a // g, b // g

def egcd(a, b):
  if b == 0:
      return a, 1, 0
  g, x1, y1 = egcd(b, a % b)
  return g, y1, x1 - (a // b) * y1

def getTokensMax100(data):
  a,b,p = KEYS['A'], KEYS['B'], KEYS['P']
  if a not in data or b not in data or p not in data: 
    print('bad input!')
    return 0
  (aX, aY), (bX,bY), (pX,pY) = data[a], data[b], data[p]
  tokenPossibilities = []
  for aCount in range(100):
    for bCount in range(100):
      if aX*aCount+bX*bCount == pX and aY*aCount+bY*bCount == pY:
        tokenPossibilities.append(aCount*3 + bCount)
  return min(tokenPossibilities, default=0)

def getClawDataWithConversionError():
  data = []
  with open('day13/inputtest.txt', 'r') as file:
    res = {}
    for line in file:
      if line.strip():
        parts = line.split(':')
        label = parts[0].strip()
        coords = parts[1].strip().split(",")
        if label=='Prize':
          x = int(coords[0].split('=')[1]) + CONVERSION_ERROR
          y = int(coords[1].split('=')[1]) + CONVERSION_ERROR
        else: 
          x = int(coords[0].split('+')[1])
          y = int(coords[1].split('+')[1])
        res[label] = (x, y)
      else: 
        data.append(res)
        res = {}
  return data

def getClawData():
  data = []
  with open('day13/input.txt', 'r') as file:
    res = {}
    for line in file:
      if line.strip():
        parts = line.split(':')
        label = parts[0].strip()
        coords = parts[1].strip().split(",")
        splitStr = '=' if label=='Prize' else '+' 
        x = int(coords[0].split(splitStr)[1])
        y = int(coords[1].split(splitStr)[1])
        res[label] = (x, y)
      else: 
        data.append(res)
        res = {}
  return data

def main():
  # print(getNumTokens()) #36571
  # print(getNumTokensWithConversionError())
  print(find_min_cost())

main()