import nmap

scanner = nmap.PortScanner()

ip = input("Enter the IP address you want to scan: ")
print("The IP you entered is: ", ip)
scanner.scan(ip, '1-1024', '-v -sS')

print(scanner.all_hosts())
