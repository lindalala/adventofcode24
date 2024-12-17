def getCalibrationResult(withConcat=False):
  results = []
  with open('day7/input.txt', 'r') as file:
    for line in file:
      res, eq = line.strip().split(': ')
      res = int(res); eq = list(map(int, eq.split()))
      isValid = isValidEquationWithConcat(res, eq) if withConcat else isValidEquation(res, eq)
      if isValid: results.append(res)
  return sum(results)

def isValidEquation(res, eq):
  if len(eq) == 0: return res == 0
  elif len(eq) == 1: return res == eq[0]
  next = eq[0]; next2 = eq[1]
  return isValidEquation(res, [next+next2] + eq[2:]) or isValidEquation(res, [next*next2] + eq[2:])

def isValidEquationWithConcat(res, eq):
  if len(eq) == 0: return res == 0 # shouldn't happen
  elif len(eq) == 1: return res == eq[0]
  next = eq[0]; next2 = eq[1]
  return isValidEquationWithConcat(res, [next+next2] + eq[2:]) \
      or isValidEquationWithConcat(res, [next*next2] + eq[2:]) \
      or isValidEquationWithConcat(res, [int(str(next)+str(next2))] + eq[2:])

def main():
  #print(getCalibrationResult()) #6231007345478
  print(getCalibrationResult(True)) #333027885676693
  #print(isValidEquation(292, [11, 6, 16, 20]))

main()