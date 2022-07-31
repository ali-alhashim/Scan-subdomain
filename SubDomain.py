import os,requests,sys

print("Please Enter your Target domain to scan for subdomain example http://google.com ")
target_domain = input()

subdomain_list = open("mySubDomain.txt").read() # open wordlist for subdomain

subdoms = subdomain_list.splitlines()           # list for each word

for sub in subdoms:
    domain_test = target_domain +"/"+ sub

    try:
        response = requests.get(domain_test, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"})
        if response.status_code ==200:
            print("Valid Domain: ", domain_test)
    except requests.ConnectionError:
        pass
    
        