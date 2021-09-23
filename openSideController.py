import subprocess

#One time setup scripts

process = subprocess.run(["scripts\\batchTester.bat", "Wasup"], capture_output=True)
print(process.stdout)

#ongoing monitoring scripts
#while True:
#  break