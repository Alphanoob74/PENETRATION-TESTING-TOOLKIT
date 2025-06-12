# Penetration Testing Toolkit
# This script provides multiple penetration testing modules including:
# 1. Port Scanner
# 2. FTP Brute Force (basic example)
# 3. HTTP Header Analyzer

import socket
import ftplib
import requests
import argparse
from datetime import datetime

# ---------------------------
# Port Scanner Module
# ---------------------------
def port_scanner(target_ip, start_port, end_port):
    print(f"\n[+] Scanning ports {start_port} to {end_port} on {target_ip}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        sock.close()
    if not open_ports:
        print("[-] No open ports found.")
    return open_ports

# ---------------------------
# FTP Brute Force Module (Simple Demo)
# ---------------------------
def ftp_brute_force(target_ip, username, password_list):
    print(f"\n[+] Attempting FTP brute-force on {target_ip} with username '{username}'")
    for password in password_list:
        try:
            ftp = ftplib.FTP(target_ip)
            ftp.login(user=username, passwd=password)
            print(f"[SUCCESS] Username: {username} | Password: {password}")
            ftp.quit()
            return password
        except ftplib.error_perm:
            continue
        except Exception as e:
            print(f"[ERROR] {e}")
            break
    print("[-] Brute-force failed. No valid credentials found.")
    return None

# ---------------------------
# HTTP Header Analyzer Module
# ---------------------------
def analyze_headers(target_url):
    print(f"\n[+] Fetching headers from {target_url}...")
    try:
        response = requests.get(target_url)
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"[ERROR] Unable to fetch headers: {e}")

# ---------------------------
# Main Menu
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("--scan", help="Run a port scan. Format: target_ip:start:end")
    parser.add_argument("--ftp", help="Run FTP brute-force. Format: target_ip:username:wordlist.txt")
    parser.add_argument("--headers", help="Analyze HTTP headers of a URL")
    args = parser.parse_args()

    if args.scan:
        try:
            target, start, end = args.scan.split(":")
            port_scanner(target, int(start), int(end))
        except:
            print("[ERROR] Invalid format for --scan. Use target_ip:start:end")

    if args.ftp:
        try:
            target, user, wordlist_file = args.ftp.split(":")
            with open(wordlist_file, 'r') as f:
                passwords = [line.strip() for line in f.readlines()]
            ftp_brute_force(target, user, passwords)
        except FileNotFoundError:
            print("[ERROR] Wordlist file not found.")
        except:
            print("[ERROR] Invalid format for --ftp. Use target_ip:username:wordlist.txt")

    if args.headers:
        analyze_headers(args.headers)

if __name__ == "__main__":
    print("\n=== Penetration Testing Toolkit ===")
    print(f"[Started] {datetime.now()}\n")
    main()
