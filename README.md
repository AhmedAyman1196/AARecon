# Reconster

The workflow followed can be found inside MyWorkFlow.png

## To run

* go into Test Directory
* update RootList.txt to the domains you want to check
* run  (while you are inside the test directory)
python ../Main.py

## Output so far

* All subdomains found in "subdomains.txt" , used sublist3r , amass , gobuster(bruteforce with a wordlist)
* Live subdomains in "livesubdomains.txt" , used httpx
* List of ips found in "ips.txt" , used nslookup
* A map between all the subdomain and the ip found , from the previous list

## To Do

* add threading
* check waybackurls for new subdomains
* reverse lookup on ips and port scanning with masscan  : 
	masscan -p <port> <CIDR Range Here> --exclude  <Exclude IP>  -- banners -oX   <Out File Name>)
* screenshot the live subdomains (aquatone or eyewitness)
* check subdomain takeover usingsubjack
* wappalyzer report for every subdomain
* create a good guide on how to rund this

## Laters

* use CRT.sh : https://github.com/ghostlulzhacks/CertificateTransparencyLogs

* github scrapping : https://github.com/gwen001/github-search/blob/master/github-subdomains.py

* alt dns for permutations : ./altdns.py -i subdomains.txt -o data_output -w words.txt -r -s output.txt 

* Knock.py : https://github.com/guelfoweb/knock , has a good output

## Notes :
you overwrite the files if they already exist (make it append ??)
