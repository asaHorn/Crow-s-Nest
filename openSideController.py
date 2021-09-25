import subprocess
import difflib
import random
import time

def main():
  #One time setup scripts
  lastRun = run('checkConnections')
  #print(run('batchTester', ['Wasup']))

  #f = open("text/testing1.txt")
  #g = open("text/testing2.txt")

  #s1 = f.read()
  #s2 = g.read()
  #print(difCheck(s1, s2))
  
  #ongoing monitoring scripts
  while True:
    print("Still alive")
    newRun = run('checkConnections')
    print(difCheck(lastRun, newRun))
    lastRun = newRun
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
        dif += "\n"
        dif += announceDiff(False, line1, line2)
        sub = True
      dif += s[-1]
    elif s[0] == "+":
      sub = False
      if add == False:
        dif += "\n"
        dif += announceDiff(True, line1, line2)
        add = True
      dif += s[-1]
  
  return(dif)
    
def announceDiff(plusOrMinus:bool, l1:int, l2:int):
  ret = ""
  if plusOrMinus:
    ret += "ADDITION"
  else:
    ret += "REMOVAL "
  ret +="|"

  if l1 == l2:
    space = getSpacer(len(str(l1)),7)
    ret += " ln:" + str(l1) + space
  else:
    space = getSpacer(len(str(l1))+len(str(l2)),9)
    ret+= " ln1:" + str(l1) + " ln2:" + str(l2) + space

  ret += "\n"

  return ret

def getSpacer(takenLen:int, targLen:int)->str:
  spacer = ""
  for _ in range(targLen-takenLen):
    spacer += " "
  return spacer

def run(script:str, arg:list=[])-> str:
  #arg.insert(0, "scripts\\" + script + ".bat")

  #process = subprocess.run(arg, capture_output=True)
  #return(process.stdout[:-2])
  if random.randrange(10) > 5:
    return """
TCP    0.0.0.0:135            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:443            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:445            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:808            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:903            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:913            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:5040           DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:27036          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49664          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49665          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49666          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49667          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49668          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49682          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49761          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49762          DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:5354         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:5354         DESKTOP-NFMARIM:49669  ESTABLISHED
TCP    127.0.0.1:5354         DESKTOP-NFMARIM:49672  ESTABLISHED
TCP    127.0.0.1:6463         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:6463         DESKTOP-NFMARIM:56768  ESTABLISHED
TCP    127.0.0.1:8307         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9010         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9010         DESKTOP-NFMARIM:49719  ESTABLISHED
TCP    127.0.0.1:9080         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9100         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9100         DESKTOP-NFMARIM:49718  ESTABLISHED
TCP    127.0.0.1:9180         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:27015        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:27060        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:45654        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:49669        DESKTOP-NFMARIM:5354   ESTABLISHED
TCP    127.0.0.1:49670        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:49671        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:49671        DESKTOP-NFMARIM:56615  ESTABLISHED
TCP    127.0.0.1:49672        DESKTOP-NFMARIM:5354   ESTABLISHED
TCP    127.0.0.1:49718        DESKTOP-NFMARIM:9100   ESTABLISHED
TCP    127.0.0.1:49719        DESKTOP-NFMARIM:9010   ESTABLISHED
TCP    127.0.0.1:56615        DESKTOP-NFMARIM:49671  ESTABLISHED
TCP    127.0.0.1:56768        DESKTOP-NFMARIM:6463   ESTABLISHED
TCP    129.21.140.228:139     DESKTOP-NFMARIM:0      LISTENING
TCP    129.21.140.228:49708   162.254.192.100:27023  ESTABLISHED
TCP    129.21.140.228:50188   do-86:https            ESTABLISHED
TCP    129.21.140.228:50769   40.83.247.108:https    ESTABLISHED
    """
  return """
TCP    0.0.0.0:135            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:443            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:445            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:808            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:903            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:913            DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:5040           DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:27036          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49664          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49665          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49666          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49667          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49668          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49682          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49761          DESKTOP-NFMARIM:0      LISTENING
TCP    0.0.0.0:49762          DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:5354         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:5354         DESKTOP-NFMARIM:49669  ESTABLISHED
TCP    127.0.0.1:5354         DESKTOP-NFMARIM:49672  ESTABLISHED
TCP    127.0.0.1:6463         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:6463         DESKTOP-NFMARIM:56768  ESTABLISHED
TCP    127.0.0.1:8307         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9010         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9010         DESKTOP-NFMARIM:49719  ESTABLISHED
TCP    127.0.0.1:9080         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9100         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:9100         DESKTOP-NFMARIM:49718  ESTABLISHED
TCP    127.0.0.1:9180         DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:27015        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:27060        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:45654        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:49669        DESKTOP-NFMARIM:5354   ESTABLISHED
TCP    127.0.0.1:49670        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:49671        DESKTOP-NFMARIM:0      LISTENING
TCP    127.0.0.1:49671        DESKTOP-NFMARIM:56615  ESTABLISHED
TCP    127.0.0.1:49672        DESKTOP-NFMARIM:5354   ESTABLISHED
TCP    127.0.0.1:49718        DESKTOP-NFMARIM:9100   ESTABLISHED
TCP    127.0.0.1:49719        DESKTOP-NFMARIM:9010   ESTABLISHED
TCP    127.0.0.1:56615        DESKTOP-NFMARIM:49671  ESTABLISHED
TCP    127.0.0.1:56768        DESKTOP-NFMARIM:6463   ESTABLISHED
TCP    129.21.140.228:139     DESKTOP-NFMARIM:0      LISTENING
TCP    129.21.140.228:49708   162.254.192.100:27023  ESTABLISHED
TCP    129.21.140.228:50188   do-86:https            ESTABLISHED
TCP    129.21.140.228:50769   40.83.247.108:https    ESTABLISHED
UDP    127.0.0.1:44594        35.142.23.10           ESTABLISHED
  """

if __name__ == '__main__':
  main()

