import subprocess

def main():
  #One time setup scripts
  print(run('batchTester'))


#ongoing monitoring scripts
#while True:
#  break

def run(script:str)-> str:
  process = subprocess.run(["scripts\\" + script + ".bat", "Wasup"], capture_output=True)
  return(process.stdout[2:-3])

if __name__ == '__main__':
  main()

