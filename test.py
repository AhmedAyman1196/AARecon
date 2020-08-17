import subprocess
import shlex

def run_command(command):
    res= [] 
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            output.strip()
    rc = process.poll()
    return rc

command = "gobuster dns -d domain -w /usr/share/wordlists/dirb/verysmall.txt"
print(run_command(command))

 
