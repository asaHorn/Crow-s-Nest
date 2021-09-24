import subprocess
import difflib
import time

def main():
  #One time setup scripts
  lastRun = run('checkConnections')
  print(run('batchTester', ['Wasup']))

  #f = open("text/testing1.txt")
  #g = open("text/testing2.txt")

  #s1 = f.read()
  #s2 = g.read()
  #print(difCheck(s1, s2))
  
  #ongoing monitoring scripts
  while True:
    newRun = run('checkConnections')
    print(difCheck(lastRun, newRun))
    time.sleep(.25)


def difCheck(s1:str, s2:str)->str:
  if s1 == s2:
    return ""

  line1 = 0
  line2 = 0
  add = False
  sub = False
  dif = ""
  for i,s in enumerate(difflib.ndiff(s1, s2)):
    if s[-1] ==  "\n":
      if s[0] == " ":
        line1 += 1
        line2 += 1
      if s[0] == "-":
        line1 += 1
      else:
        line2 += 1
    
    if s[0] == " ":
      add = False 
      sub = False
    elif s[0] == "-":
      add = False
      if sub == False:
        dif += announceDiff(False, line1, line2)
        sub = True
      dif += s[-1]
    elif s[0] == "+":
      sub = False
      if add == False:
        dif += announceDiff(True, line1, line2)
        add = True
      dif += s[-1]
  
  return(dif)
    
def announceDiff(plusOrMinus:bool, l1:int, l2:int):
  ret = ""
  ret += "} "
  if plusOrMinus:
    ret += "+"
  else:
    ret += "-"
  ret +="|"

  if l1 == l2:
    ret += "ln:" + str(l1)
  else:
    ret+= "ln1:" + str(l1) + " ln2:" + str(l2)
  
  ret += "{"

  return ret

def run(script:str, arg:list=[])-> str:
  arg.insert(0, "scripts\\" + script + ".bat")

  process = subprocess.run(arg, capture_output=True)
  return(process.stdout[:-2])

if __name__ == '__main__':
  main()

