import subprocess
import sublist3r
import shlex
import subprocess
from termcolor import colored

class subdomainer:
	def __init__(self, domainList , sublisterOn , amassOn , gobustOn , wordlist):

		self.domainList = domainList  # holds the list of root domains
		self.allsubdomains = []		  # holds the list of all subdmains found
		self.dict = {}				  # Map between the domain and the subdomains
		self.wordlist = wordlist 	  # holds the wordlist used in bruteforcing
		self.subdomains = []
		self.livesubdomains = []

		for domain in domainList:
			print(colored("Enumerating ",'red') , domain)
			self.subdomains = []
			
			if(sublisterOn):
				self.subdomains.extend(self.sublister(domain)) 
				self.updateFiles()
			
			# if(amassPassiveOn):
			# 	self.subdomains.extend(self.amassPassive(domain))
			# 	self.updateFiles()

			if(amassOn):		
				self.subdomains.extend(self.amass(domain))
				self.updateFiles()

			if(gobustOn):
				self.subdomains.extend(self.gobust(domain))
				self.updateFiles()

		# combining all into one text file
		self.allsubdomains = sorted(set(self.allsubdomains))
		if len(self.allsubdomains) > 1:
			print(colored("Combining gathered subdomains to  subdomains.txt ",'red'))
			f = open("subdomains.txt", "w")
			for i in self.allsubdomains:
				splitted = i.split(".com")
				for k in splitted:
					if(k!=""):
						f.write(k.strip()+".com\n")
			f.close()
			print(colored("Done Added subdomains.txt ",'green'))
		else:
			print(colored("No subdomains found" , "red"))

		# creating a list of live subdomains
		self.checkLive()
		self.livesubdomains = sorted(set(self.livesubdomains))
		if len(self.livesubdomains) > 1:
			f = open("livesubdomains.txt", "w")
			for i in self.livesubdomains:
				splitted = i.split(".com")
				for k in splitted:
					if(k!=""):
						f.write(k.strip()+".com\n")
			f.close()
			print(colored("Done Added livesubdomains.txt ",'green'))
		else:
			print(colored("No Live Subdomains Found!" , "red"))

# enumeration using https://github.com/aboul3la/Sublist3r
	def sublister(self, domain):
		print(colored("- Started Sublist3r ...",'blue'))
		subdomains = sublist3r.main(domain,40, savefile=None, ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)
		subdomains = [w.replace('<BR>', '\n') for w in subdomains]
		return subdomains


# This turned out to be redundant to the next step
# amass enum -passive -d target.com
	# def amassPassive(self , domain):
	# 	print(colored("- Started Amass Passive",'blue'))
	# 	command = "amass enum -passive -d " + domain  +" --silent"
	# 	res = run_command(command)
	# 	return res

#amass enum -brute -d target.com
	def amass(self, domain):
		print(colored("- Started Amass ... ",'blue'))
		command = "amass enum  -d " + domain 
		res = run_command(command)
		return res

# gobuster dns -d target.com -w subdomaiinWordList.txt
	def gobust(self,domain):
		print(colored("- Started Gobuster ...",'blue'))
		command = "gobuster dns -d " + domain + " -w "+self.wordlist + " --quiet"
		res = run_command(command)
		return res

# updates the subdomains files		
	def updateFiles(self):

		for domain in self.domainList:
			self.allsubdomains.extend(self.subdomains)
			self.dict[domain] = self.subdomains

			filename = domain + ".subdomains.txt"
			f = open(filename, "w")
			self.dict[domain] = sorted(set(self.dict[domain]))
			for j in self.dict[domain]:
				splitted = j.split(".com")
				for k in splitted:
					if(k!=""):
						f.write(k.strip()+".com\n")

			print(colored("Updated "+filename,'green'))
			f.close()

# 	httpx -l subdomains.txt
	def checkLive(self):
		print(colored("Checking Live subdomains ...",'green'))
		command = "httpx -l subdomains.txt -silent"
		res = run_command(command)
		self.livesubdomains = res

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
		print("!!!!!!!!!    start !!!!!!!!")
		print(" All domains enumerated are :")
		for i in self.domainList:
			print( i)
		print("\nAll subdomains found")
		for i in self.allsubdomains:
			print( i)
		print("\n Map")
		for i in self.domainList:
			print ("domain:",i)
			for j in self.dict[i]:
				print(j)

		return ""