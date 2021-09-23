import subprocess

#One time setup scripts

string = subprocess.run(["batchTester.bat", "Wasup"], capture_output=True)
print(string)

#ongoing monitoring scripts
while True:
  break