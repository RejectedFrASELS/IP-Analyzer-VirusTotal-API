# IP-Analyzer-VirusTotal-API

This tool scans IP Addresses from an excel file using VirusTotal API and reports to you.

You can run the code in any directory, the code will search for excel files in that directory and lets you select which file's which column has IP addresses.
The code will create a txt file report.

To run the code you need to get an API from Virus Total. More information at: https://support.virustotal.com/hc/en-us/articles/115002100149-API

## How to Use

### Requirements:
1. Python 3
2. Some python libraries: requests, json, openpyxl, glob, os
3. Some excel file with IP addresses in a column

### Usage:
1. Insert your API in code
2. Simply run it by typing ```python IPChecker.py``` or however you want.
3. Select the excel file and other credentials.
4. You can find the report in same directory after running the code.
