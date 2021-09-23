import subprocess

def main():
  #One time setup scripts
  print(run('batchTester', ['Wasup']))
  print(run('checkConnections', ['Wasup']))


#ongoing monitoring scripts
#while True:
#  break

def run(script:str, arg:list=[])-> str:
  print(arg)
  arg.insert(0, "scripts\\" + script + ".bat")

  process = subprocess.run(arg, capture_output=True)
  return(process.stdout[:-2])

if __name__ == '__main__':
  main()

