def getOutput(data):
  a,b,c,p = data['a'], data['b'], data['c'], data['p']
  i = 0
  output = []
  while i < len(p)-1:
    op = p[i+1]
    match p[i]:
      case 0: a=a//(2**(getCombo(op,a,b,c)))
      case 1: b=b^op
      case 2: b=getCombo(op,a,b,c)%8
      case 3: 
        if a!=0: 
          i = op
          continue
      case 4: b=b^c
      case 5: output.append(getCombo(op,a,b,c)%8)
      case 6: b=a//(2**(getCombo(op,a,b,c)))
      case 7: c=a//(2**(getCombo(op,a,b,c)))
      case _: print('unknown op: ', p[i])
    i+=2
  return output

def getCombo(operand,a,b,c):
  if 0<=operand<=3: return operand
  if operand == 4: return a
  if operand == 5: return b
  if operand == 6: return c
  print('invalid operand: ', operand)
  return None

def getAToRepeat(data):
  p = data['p']
  data['a'] = int('0o0',8)
  a='0o1'
  for target in reversed(p):
    options = []
    for i in range(8):
      a = a[:-1] + str(i)
      data['a'] = int(a,8)
      out = getOutput(data)
      if out[0] == target:
        options.append(a)
    print(a)
    a += '0'
  return data['a']

def main():
  testData = {'a': int('0o1035510005136764',8), 'b': 0, 'c': 0, 'p':[2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0]}
  testData2 = {'a': 2024, 'b': 0, 'c': 0, 'p':[0,3,5,4,3,0]}
  data = {'a': 27575648, 'b': 0, 'c': 0, 'p':[2,4,1,2,7,5,4,1,1,3,5,5,0,3,3,0]}
  # print(','.join(map(str, getOutput(data)))) #1,7,2,1,4,1,5,4,0
  print(getOutput(testData)) # i manually brute forced it lol
  # print(getAToRepeat(data))

main()