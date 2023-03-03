import requests
import json
import openpyxl
import glob
import os

print("""
 ___ ____        _                _                     __     _______ 
 |_ _|  _ \     / \   _ __   __ _| |_   _ _______ _ __  \ \   / /_   _|
  | || |_) |   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|  \ \ / /  | |  
  | ||  __/   / ___ \| | | | (_| | | |_| |/ /  __/ |      \ V /   | |  
 |___|_|     /_/   \_\_| |_|\__,_|_|\__, /___\___|_|       \_/    |_|  
                                    |___/                                                                        
 This tool scans IP Addresses from an excel file using VirusTotal API and reports to you.
                                
                                By RejectedFrASELS
 """)

# Use the glob module to find all Excel files in the directory
excel_files = glob.glob(os.path.join('*.xlsx'))

# Print the list of Excel files in the directory
if len(excel_files) > 0:
    print("\nExcel files in directory:")
    for i, file in enumerate(excel_files):
        print(f"{i+1}. {os.path.basename(file)}")
else:
    print("\nNo Excel files found in directory.")
    exit()

# Prompt the user to select an Excel file from the list
selected_file_index = int(input("Select an Excel file (enter the number): "))
if selected_file_index < 1 or selected_file_index > len(excel_files):
    print("Invalid selection.")

# Get the file name of the selected Excel file
selected_file_name = os.path.basename(excel_files[selected_file_index-1])
print(f"Selected file: {selected_file_name}")
# Load the Excel file
workbook = openpyxl.load_workbook(selected_file_name)

#Select the worksheet you want to read from
print("\nEnter the Worksheet's name that has the IP Addresses(usually is 'Sheet1'):")
sheet = input()
worksheet = workbook[sheet]


# Get the values from the column you want to use
print("\nEnter the Column that has the IP Addresses:")
column = input()
print("\nSelected column "+column+" \n")

column_values = [cell.value for cell in worksheet[column]]

no_duplicated_column_values = list(set(column_values)) #ayni ipleri teke indir

#print(no_duplicated_column_values)

# Open the output file
with open('output.txt', 'w') as f:
    # Use the values in a for loop
    for value in no_duplicated_column_values:
        base_url = "https://www.virustotal.com/api/v3/ip_addresses/"
        url = f"{base_url}{value}"

        headers = {
            "accept": "application/json",
            "x-apikey": "APIKEY" #API KEY HERE
        }

        response = requests.get(url, headers=headers)
        json_file = json.loads(response.text)

        ip_address = json_file["data"]["id"]
        as_owner = json_file["data"]["attributes"]["as_owner"]
        last_analysis_stats = json_file["data"]["attributes"]["last_analysis_stats"]

        print(f"IP Address: {ip_address}")
        print(f"AS Owner: {as_owner}")
        print("Last Analysis Stats:")
        for engine, result in last_analysis_stats.items():
            if isinstance(result, dict):
                category = str(result['category'])
                method = str(result['method'])
                print(f"\t{engine}: {category} ({method})")
            else:
                print(f"\t{engine}: {result}")
        print("="*50)        


        f.write(f"IP Address: {ip_address}\n")
        f.write(f"AS Owner: {as_owner}\n")
        f.write("Last Analysis Stats:\n")
        for engine, result in last_analysis_stats.items():
            if isinstance(result, dict):
                category = str(result['category'])
                method = str(result['method'])
                f.write(f"\t{engine}: {category} ({method})\n")
            else:
                f.write(f"\t{engine}: {result}\n")
        f.write("="*50 + "\n")

print("The output also created as a .txt file in same directory. \n Press 'Enter' to exit")
x = input()
