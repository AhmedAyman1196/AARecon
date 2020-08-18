import subprocess
import sublist3r
import shlex
import subprocess
from termcolor import colored

class ipWorker:
	def __init__(self, subdomainsList ):
		self.subdomains = subdomainsList  	# holds the list of subdomains domains
		self.ips  = []						# holds the list of ips
		self.dict = {} 						# maps the subdomain to the ip

		# nsloopkup on all subdomains given
		for sub in self.subdomains:
			iplist = self.lookup(sub)
			self.dict[sub] = [] 
			for j in range(0,len(iplist)):
				if(iplist[j][0:4]=="Name"):
					ip = iplist[j+1][9:]
					self.ips.append(ip)
					self.dict[sub].append(ip)


		# writing out all ips to ips.txt
		self.ips = sorted(set(self.ips))
		filename = "ips.txt"
		f = open(filename, "w")
		for ip in self.ips:
			f.write(ip+"\n")
		f.close()

		print(colored("added all ips to  "+filename,'green'))

		# writing out a map between subdmain and ip
		self.ips = sorted(set(self.ips))
		filename = "ipmap.txt"
		f = open(filename, "w")
		for sub in self.dict:
			f.write(sub+" : \n")
			if(len(self.dict[sub])==0):
				f.write("No ips found\n")
			for ip in self.dict[sub]:
				f.write(ip+"\n")
		f.close()

		print(colored("added ipmap.txt which shows the ip belongs to which subdomain",'green'))


# enumeration using https://github.com/aboul3la/Sublist3r
	def lookup(self, subdomain):
		print(colored("nslookup on %s" % subdomain,'blue'))
		command = "nslookup " + subdomain 
		res = run_command(command)
		return res

# runs a bash command
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

# how we print this class (for debugging)    	
	def __str__(self):
		
		return ""