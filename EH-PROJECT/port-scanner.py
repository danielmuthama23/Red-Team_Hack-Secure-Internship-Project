import socket
import argparse
from datetime import datetime

def port_scanner(target, start_port, end_port):
    open_ports = []
    # Loop through specified port range
    for port in range(start_port, end_port + 1):
        try:
            # Create a TCP socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Timeout to skip closed ports
                # Attempt connection
                result = s.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"[+] Port {port} is open")
                s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            exit()
        except socket.gaierror:
            print("[!] Invalid hostname.")
            exit()
        except socket.error:
            print("[!] Connection error.")
            exit()
    return open_ports

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Basic Port Scanner")
    parser.add_argument("target", help="Target IP or domain (e.g., testphp.vulnweb.com)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Starting port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Ending port (default: 1024)")
    args = parser.parse_args()

    # Banner
    print("-" * 50)
    print(f"Scanning target: {args.target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    # Run scan
    open_ports = port_scanner(args.target, args.start, args.end)

    # Results
    print("\nScan complete!")
    print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    main()