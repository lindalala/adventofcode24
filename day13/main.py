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
    tokens += getTokens(data)
  return tokens

def getTokens(data):  
  a,b,p = KEYS['A'], KEYS['B'], KEYS['P']
  if a not in data or b not in data or p not in data: 
    print('bad input!')
    return 0
  (aX, aY), (bX,bY), (pX,pY) = data[a], data[b], data[p]
  bCount = (aX*pY-aY*pX)//(bY*aX-bX*aY)
  aCount = (pX-bX*bCount)//aX
  if aX*aCount+bX*bCount == pX and aY*aCount+bY*bCount == pY:
    return aCount*3 + bCount
  return 0

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
  with open('day13/input.txt', 'r') as file:
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
  if res not in data and len(res)>0: data.append(res)
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
  print(getNumTokensWithConversionError()) # 85527711500010

main()