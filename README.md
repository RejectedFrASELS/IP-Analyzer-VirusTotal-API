# IP-Analyzer-VirusTotal-API

This tool scans IP Addresses from an excel file or txt file using VirusTotal API and reports to you.

You can run the code in any directory, the code will search for excel files in that directory and lets you select which file's which column has IP addresses.
The code will create a txt file report.

If you willing to check the IPs from an txt file, paste them line by line in iplist.txt and run ```IPCheckerTXT.py```

To run the code you need to get an API from Virus Total. More information at: https://support.virustotal.com/hc/en-us/articles/115002100149-API

#### This code also implemented in a Web App
See here: [SOC-Tool-Box](https://github.com/RejectedFrASELS/SOC-Tool-Box)

## How to Use

### Requirements:
1. Python 3
2. Some python libraries: ```pip install -r requirements.txt```
3. Some excel file or txt file with IP addresses in a column

### Usage:
1. Insert your API Keys in ```IPChecker-apikeys.txt``` line by line. You can use multiple API Keys.
2. Install libraries: ```pip install -r requirements.txt```
3. Simply run it by typing ```python IPChecker.py``` ```python IPCheckerTXT.py``` or however you want.
4. Select the excel file and other credentials.
5. You can find the report in same directory after running the code.
