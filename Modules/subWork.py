import subprocess
import sublist3r 
from subprocess import Popen, PIPE
from termcolor import colored

class subdomainer:
	def __init__(self, domainList , sublisterOn , amassPassiveOn , amassBruteOn , gobustOn , wordlist):

		self.domainList = domainList  # holds the list of root domains
		self.allsubdomains = []		  # holds the list of all subdmains found
		self.dict = {}				  # Map between the domain and the subdomains
		self.wordlist = wordlist
		self.subdomains = []

		for domain in domainList:
			print(colored("Enumerating ",'red') , domain)
			self.subdomains = []
			
			if(sublisterOn):
				self.subdomains.extend(self.sublister(domain)) 
				self.updateFiles()
			
			if(gobustOn):
				self.subdomains.extend(self.gobust(domain))
				self.updateFiles()
			
			if(amassPassiveOn):
				self.subdomains.extend(self.amassPassive(domain))
				self.updateFiles()

			if(amassBruteOn):		
				self.subdomains.extend(self.amassBrute(domain))
				self.updateFiles()


		# combining all into one text file
		self.allsubdomains = sorted(set(self.allsubdomains))
		if len(self.allsubdomains) > 1:
			print(colored("Combining gathered subdomains to  subdomains.txt ",'red'))
			f = open("subdomains.txt", "a")
			for i in self.allsubdomains:
				splitted = i.split(".com")
				for k in splitted:
					if(k!=""):
						f.write(k.strip()+".com\n")
			f.close()
			print(colored("Done Added subdomains.txt ",'green'))
		else:
			print(colored("No subdomains found" , "red"))


# enumeration using https://github.com/aboul3la/Sublist3r
	def sublister(self, domain):
		print(colored("- Started Sublist3r",'blue'))
		subdomains = sublist3r.main(domain,40, savefile=None, ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)
		subdomains = [w.replace('<BR>', '\n') for w in subdomains]
		return subdomains

	
# amass enum -passive -d target.com
	def amassPassive(self , domain):
		print(colored("- Started Amass Passive",'blue'))
		res = []
		process = subprocess.Popen(['amass', "enum" ,"-passive", "-d" ,domain], 
						   stdout=subprocess.PIPE,
						   universal_newlines=True)
		while True:
			output = process.stdout.readline()
			res.append(output.strip())
	
			return_code = process.poll()
			if return_code is not None:
				for output in process.stdout.readlines():
					res.append(output.strip())
					break
		return res

#amass enum -brute -d target.com
	def amassBrute(self, domain):
		print(colored("- Started Amass Brute force",'blue'))

		res = []
		process = subprocess.Popen(['amass', "enum" ,"-brute", "-d" ,domain], 
						   stdout=subprocess.PIPE,
						   universal_newlines=True)
		while True:
			output = process.stdout.readline()
			res.append(output.strip())
	
			return_code = process.poll()
			if return_code is not None:
				for output in process.stdout.readlines():
					res.append(output.strip())
					break
		return res

# gobuster dns -d target.com -w subdomaiinWordList.txt
	def gobust(self,domain):
		res = []
		# if !self.bruteforce: # will only work if brute force is on
		# 	return res

		print(colored("- Started Gobuster",'blue'))

		process = subprocess.Popen(['gobuster', "dns" ,"-d", domain,"-w" , self.wordlist], 
						   stdout=subprocess.PIPE,
						   universal_newlines=True)
		while True:
			output = process.stdout.readline()
			res.append(output.strip())
	
			return_code = process.poll()
			if return_code is not None:
				for output in process.stdout.readlines():
					res.append(output.strip())
					break
		return res

# updates the subdomains files		
	def updateFiles(self):

		for domain in self.domainList:
			self.allsubdomains.extend(self.subdomains)
			self.dict[domain] = self.subdomains

			filename = domain + ".subdomains.txt"
			f = open(filename, "a")
			self.dict[domain] = sorted(set(self.dict[domain]))
			print("here")
			for j in self.dict[domain]:
				splitted = j.split(".com")
				for k in splitted:
					if(k!=""):
						f.write(k.strip()+".com\n")

			print(colored("Updated "+filename,'green'))
			f.close()
	

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