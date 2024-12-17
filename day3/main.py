import re

def getMemStr():
  mem = ''
  with open('day3/input.txt', 'r') as file:
      for line in file:
        mem += line
  return mem

def getRes(mem):
  res = 0
  reg = re.compile(r"mul\((\d+),(\d+)\)")
  for (a,b) in reg.findall(mem):
      a = int(a); b = int(b)
      if a <= 999 and b <= 999:
          res += a*b
  return res

def getResWithDonts(mem):
  res = 0
  reg = re.compile(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))")
  doing = True
  for (a,b,dont,do) in reg.findall(mem):
      if dont != '': doing = False
      elif do != '': doing = True
      elif doing:
        a = int(a); b = int(b)
        if a <= 999 and b <= 999:
            res += a*b
  return res
   

def main():
  mem = getMemStr()
  print(getRes(mem)) #174103751
  print(getResWithDonts(mem)) #100411201

main()

        