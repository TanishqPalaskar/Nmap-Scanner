import os

def run_nmap_scan(ip):
    # List of Nmap scanning options
    options = {
        "1": "-sS (Stealth Scan)",
        "2": "-sT (TCP Connect Scan)",
        "3": "-A (Aggressive Scan with OS and version detection)",
        "4": "-p- (Scan all 65535 ports)",
        "5": "-sU (UDP Scan)",
        "6": "-sV (Version Detection)",
        "7": "-O (OS Detection)",
        "8": "--top-ports 1000 (Scan top 1000 most common open ports)",
        "9": "Specific port scan (Ask for port input)",
        "10": "--script vuln (Scan for vulnerabilities)",
        "11": "-sC (Default script scan)",
        "12": "-T4 (Aggressive timing scan for faster execution)",
        "13": "--traceroute (Trace route to host)",
        "14": "--reason (Display reason for host up/down)",
        "15": "-Pn (No ping, assumes host is up)"
    }

    # Display options to the user
    print("\nChoose a scan type:")
    for key, value in options.items():
        print(f"{key}: {value}")
    
    # Get the user's choice
    choice = input("\nEnter the number of the scan type you want to run: ")

    # Handle specific port scan option
    if choice == "9":
        port = input("Enter the specific port you want to scan (e.g., 80, 443): ")
        command = f"nmap -p {port} {ip}"
    else:
        # Get the corresponding Nmap command
        nmap_command = options.get(choice)
        if nmap_command:
            if choice == "8":
                command = f"nmap --top-ports 1000 {ip}"
            else:
                scan_option = nmap_command.split()[0]
                command = f"nmap {scan_option} {ip}"
        else:
            print("Invalid option selected.")
            return

    # Execute the Nmap command
    print(f"\nRunning: {command}")
    os.system(command)

if __name__ == "__main__":
    # Ask for the IP to scan
    target_ip = input("Enter the IP address you want to scan: ")

    # Run the scan with the selected option
    run_nmap_scan(target_ip)
