import socket
with open("subdomains.txt", "r") as ins:
    for line in ins:
        print (socket.gethostbyname(line.strip()))


        nslookup account.acronis.com

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