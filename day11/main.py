SEEN = {}

def blinkLen(input, iterations):
  stones = list(map(int, input.split()))
  count = 0
  for stone in stones:
    count += blinkLenHelper(stone, iterations, 0)
  return count

def blinkLenHelper(stone, iterations, step):
  if (stone, iterations-step) in SEEN: 
    return SEEN[(stone, iterations-step)]
  if step == iterations: return 1
  if stone == 0: res = blinkLenHelper(1, iterations, step+1)
  else:
    stoneStr = str(stone)
    stoneLen = len(stoneStr)
    if stoneLen%2 == 0:
      res = blinkLenHelper(int(stoneStr[:stoneLen//2]), iterations, step+1) + \
            blinkLenHelper(int(stoneStr[stoneLen//2:]), iterations, step+1)
    else:
      res = blinkLenHelper(stone*2024, iterations, step+1)
  SEEN[(stone, iterations-step)] = res
  return res

def blinkLenDumb(input, n):
  next = list(map(int, input.split()))
  for _ in range(n):
    next = blinkDumb(next)
  return len(next)

def blinkDumb(input):
  res = []
  for stone in input:
    if stone == 0:
      res.append(1)
      continue
    stoneStr = str(stone)
    stoneLen = len(stoneStr)
    if stoneLen%2 == 0:
      res.append(int(stoneStr[:stoneLen//2]))
      res.append(int(stoneStr[stoneLen//2:]))
    else:
      res.append(stone*2024)
  return res
     
def main():
  input = '17639 47 3858 0 470624 9467423 5 188'
  testInput = '125 17'
  # print(blinkLen(testInput, 6)) #22
  # print(blinkLen(testInput, 25)) #55312
  print(blinkLen(input, 75)) #240884656550923

main()