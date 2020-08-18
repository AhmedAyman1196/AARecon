# import the os module
import os
from termcolor import colored
from Modules import *

#test
# detect the current working directory and print it
path = os.getcwd()
print (colored("\nWe are currently working in %s" % path , "blue"))

# Read Root domains
rootList_Filename = "Files/RootList.txt"
print (colored("Reading list of root domains from  %s\n" % rootList_Filename , "blue"))

with open(rootList_Filename) as f:
    rootList = f.readlines()

# looping on every domain
print(colored("Found :" , "green"))
domainList = []
for domain in rootList:
	domain= domain.strip() # removing spaces , line breaks, etc..
	print(domain)
	domainList.append(domain)

# subdomain enumeration
print(colored("\n------------------------------", 'red'))
print(colored("Started Subdomian enumeration",'green'))
print(colored("------------------------------\n",'red'))


sublisterOn = True 
amassOn = False
gobustOn = False
subwordlist = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt"	# change this to the wordlist of you choice
subwordlist = "/usr/share/wordlists/dirb/verysmall.txt"	# change this to the wordlist of you choice

subdomainer = subWork.subdomainer(domainList , sublisterOn, amassOn , gobustOn , subwordlist)

ipWorker = ipWork.ipWorker(subdomainer.subdomains)
#note:  check if it should be changed to subdomainer.livesubdomains
