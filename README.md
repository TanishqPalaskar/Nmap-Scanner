## Nmap Automated Scanning Tool

This tool automates Nmap scanning with various scan types. It prompts the user to input an IP address, and based on the selected scan option, it executes the corresponding Nmap command.

### Features:
- **All Scans**: Comprehensive scanning using `-A` for aggressive mode.
- **Version Detection**: Uses `-sV` to detect service versions.
- **Operating System Detection**: Employs `-O` to detect the operating system.
- **TCP SYN Scan**: Quick scan with `-sS`.
- **UDP Scan**: Scans UDP ports with `-sU`.
- **Top 1000 Ports**: Scans the most common open ports.
- **Custom Port Scan**: Asks you for a specific port to scan.
- **Full TCP Scan**: Scans all 65535 TCP ports.
- **Ping Scan**: Discovers live hosts on the network.
- **Firewall Evasion**: Evades firewalls using `-D` for decoy scans.

### Usage:
1. Run the script.
2. Input the target IP address.
3. Choose the desired scan option from the menu.
4. The tool will run the Nmap scan with the selected options and display the output.
