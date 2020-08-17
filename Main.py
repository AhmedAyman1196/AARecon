# import the os module
import os
from termcolor import colored
from Modules import *

# detect the current working directory and print it
path = os.getcwd()
print (colored("We are currently working in %s\n" % path) , "blue")

# Read Root domains
rootList_Filename = "Files/RootList.txt"

with open(rootList_Filename) as f:
    rootList = f.readlines()

# looping on every domain
domainList = []
for domain in rootList:
	domain= domain.strip() # removing spaces , line breaks, etc..
	domainList.append(domain)

# subdomain enumeration
print(colored("------------------------------", 'red'))
print(colored("Started Subdomian enumeration",'green'))
print(colored("------------------------------\n",'red'))

sublisterOn = True 
amassPassiveOn = False
amassBruteOn = False
gobustOn = True
subwordlist = "/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt"	# change this to the wordlist of you choice
subwordlist = "/usr/share/wordlists/dirb/verysmall.txt"	# change this to the wordlist of you choice

# arguments( domainList , sublisterOn , amassPassiveOn , amassBruteOn , gobustOn ,subwordlist):
subdomainer = subWork.subdomainer(domainList , sublisterOn, amassPassiveOn ,
 amassBruteOn , gobustOn , subwordlist)

