#code for nslookup tools
utake=input("give url? ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("----------> nslookup tools all command baase on your target <-------------------")
print("\n")
print(f"nslookup -type=A {utake}")
print(f"nslookup -type=AAAA {utake}")
print(f"nslookup -type=CNAME {utake}")
print(f"nslookup -type=MX {utake}")
print(f"nslookup -type=SOA {utake}")
#code for dig tools
print(f'''nslookup -type=TXT {utake}\n----------> dig tools all command baase on your target <-------------------\n\ndig {utake} A\ndig {utake} AAAA\ndig {utake} CNAME\ndig {utake} TXT\ndig {utake} SOA\ndig {utake} MX''')
print("\n")
print("----------> host tools all command baase on your target <-------------------")
print("\n")
# for host tools
print(f"host {utake}")
print("\n")
# we skip dnsrecon for i get some problem insidde of this tools

# for code wafw00f tools
print("-----------> waw00f tools all comman for <-------------")
print("This tools use for fire-wal detectio and fire-wal information of target website")
print("\n")
print(f"wafw00f {utake}")

print("")
# code for passive recon web tools
print("-----------> website for recon <-------------")
print("\n")
print("https://dnsdumpster.com")
print("https://shodan.io")
print("https://sitereport.netcraft.com")
print("https://whois.domaintools.com")
print("https://web-check.as93.com")



