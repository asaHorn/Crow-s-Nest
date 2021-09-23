import subprocess

#One time setup scripts

string = subprocess.run(["scripts/batchTester.bat", "Wasup"], capture_output=True)
print(string)

#ongoing monitoring scripts
while True:
  continue