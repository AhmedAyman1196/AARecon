import subprocess
import shlex

def run_command(command):
    res= [] 
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=None)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            res.append(output.decode("utf-8").strip())
    rc = process.poll()
    return res

command = "gobuster dns -d google.com -w /usr/share/wordlists/dirb/verysmall.txt --quiet"
res = run_command(command)
for i in res:
    print(i)