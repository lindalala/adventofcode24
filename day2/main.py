safeCount = 0

def isSafeHelper(a,b,isInc):
  if isInc and not b>a: return False
  if not isInc and not a>b: return False
  diff = abs(b-a)
  if diff < 1 or diff > 3: return False
  return True

def isSafe(r):
  isInc = r[-1]>r[0]
  for i in range(1, len(r)):
    if not isSafeHelper(r[i-1], r[i], isInc): return False
  return True

with open('day2/input.txt', 'r') as file:
    for line in file:
        r = [int(i) for i in line.strip().split()]
        if isSafe(r): safeCount +=1
        else:
           for i in range(0,len(r)):
              if isSafe(r[:i] + r[i+1:]): 
                safeCount+=1
                break

print(safeCount) # 612
