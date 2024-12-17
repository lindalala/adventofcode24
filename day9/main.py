def getChecksum(moveFiles=False):
  diskMap = None
  with open('day9/input.txt', 'r') as file:
    for line in file:
      diskMap = line
  return getCheckSumHelper(diskMap, moveFiles)

def getCheckSumHelper(diskMap, moveFiles=False):
  blocks = getBlocks(diskMap)
  compacted = compactBlocksWithFiles(blocks) if moveFiles else compactBlocks(blocks) 
  return sum(i * c for i, c in enumerate(compacted) if c is not None)

def getBlocks(diskMap):
  id = 0
  blocks = []
  for di, d in enumerate(diskMap):
    d = int(d)
    for i in range(d):
      if di%2 == 0: # id
        blocks.append(id)
        if i == d-1: id += 1
      else: # free space
        blocks.append(None)
  return blocks

def compactBlocks(blocks):
  for bi,b in reversed(list(enumerate(blocks))):
    if None not in blocks: break
    if b is not None: blocks[blocks.index(None)] = b
    del blocks[bi] 
  return blocks

def getNones(blocks, maxI):
  nones = {}
  idx,count = 0,0
  for bi,b in enumerate(blocks):
    if bi > maxI: break
    if b is None:
      count += 1
      if bi == len(blocks)-1 or blocks[bi+1] is not None:
        nones[idx+1] = count
        count = 0
    else:
      idx = bi
  return nones

def compactBlocksWithFiles(blocks):
  fileLen = 0
  curID = blocks[-1]
  curI = len(blocks)-1
  nones = getNones(blocks, curI)

  for bi,b in reversed(list(enumerate(blocks))):
    if None not in blocks: break
    if b == curID: 
      fileLen += 1
    else:
      if curID is not None: 
        freeIdx = min([ni for ni,nc in nones.items() if nc >= fileLen], default=10**100)
        if freeIdx < curI:
          for i in range(fileLen):
            blocks[i+freeIdx] = curID
            blocks[curI-i] = None
          nones = getNones(blocks, bi)
      curID = b
      fileLen = 1 
      curI = bi
  return blocks

def main():
  test = '2333133121414131402'
  # print(getCheckSumHelper(test, True))
  # print(getChecksum()) # 6367087064415
  print(getChecksum(True)) # 6390781891880

main()