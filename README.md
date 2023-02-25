# IP-Analyzer-VirusTotal-API

This tool scans IP Addresses in an excel file and reports to you using VirusTotal API

You can run the code in any directory, the code will search for excel files in that directory and lets you select which file's which column that has IP addresses.
The code will create a txt file report.

To run the code you need to get an API from Virus Total. More information on: https://support.virustotal.com/hc/en-us/articles/115002100149-API

## How to Use

### Requirements:
1. Python 3
2. Some python libraries: requests, json, openpyxl, glob, os
3. Some excel file with IP addresses in a column

### Usage:
1. Insert your API in code
2. Simply run it typing ```python IPChecker.py``` or however you want.
3. Select the excel file and other credentials.
4. You can find the report after running the code in same directory.
