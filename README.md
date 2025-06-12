 PENETRATION-TESTING-TOOLKIT

  COMPANY : CODTECH IT SOLUTIONS

  NAME : MUZAMMIL AHMED

  INTERN ID : CT06DF444

  DOMAIN : CYBER SECURITY & ETHICAL HACKING

  DURATIONS : 6 WEEK

  MENTOR : NEELA SANTOSH

 ## DESCRIPTION ## 
 

 🧰 Penetration Testing Toolkit – Python CLI

All-in-One Offensive Security Toolkit
A powerful command-line Python script that brings together essential penetration testing modules—from port scanning and brute-forcing to HTTP analysis—into a single, beginner-friendly yet effective tool for ethical hackers and cybersecurity learners.

🔍 Modules Included

  🔓 Port Scanner
  
        Efficiently scans a range of ports on a target IP to detect open services.

   📂 FTP Brute Force (Demo)
   
        Performs a basic dictionary-based brute force attack on FTP services to test login credentials.

  🧾 HTTP Header Analyzer
  
        Fetches and displays all HTTP headers from a target URL to identify potential misconfigurations or useful reconnaissance data.

⚙️ Technologies Used

Library	                     Purpose
socket	                     Low-level TCP/IP port scanning
ftplib	                     FTP connection and login attempts
requests	                   HTTP GET requests for headers
argparse	                   Clean command-line interface
datetime	                   Logging the start time of a scan

🚀 How to Use

  Make sure you have Python 3 installed.

  Run the script from your terminal with any of the following options:

🔍 Port Scanner

     python Penetration_Testing_Toolkit.py --scan 192.168.1.1:20:100
     
Scans ports 20 to 100 on 192.168.1.1.

💥 FTP Brute Force (Demo)

       python Penetration_Testing_Toolkit.py --ftp 192.168.1.1:admin:wordlist.txt
       
Tries passwords from wordlist.txt on FTP service at 192.168.1.1 with username admin.

🌐 HTTP Header Analysis

       python Penetration_Testing_Toolkit.py --headers http://example.com

Displays all HTTP response headers from the given URL.


💡 Use Cases

    🔐 Pentesting lab exercises

    🎓 Cybersecurity learning projects

    🔎 Quick on-the-go recon and enumeration

    📂 Testing basic security posture of small servers
    

⚠️ Disclaimer

This toolkit is intended for educational and ethical testing only.
⚠️ Do NOT scan or attack systems without proper authorization.

###  OUTPUT   ###

![Image](https://github.com/user-attachments/assets/106e733f-df40-4d35-9d3c-490e3f15a792)
