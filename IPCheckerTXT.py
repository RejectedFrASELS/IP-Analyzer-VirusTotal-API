import requests
import json
from datetime import datetime

print("""
 ___ ____        _                _                     __     _______ 
 |_ _|  _ \     / \   _ __   __ _| |_   _ _______ _ __  \ \   / /_   _|
  | || |_) |   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|  \ \ / /  | |  
  | ||  __/   / ___ \| | | | (_| | | |_| |/ /  __/ |      \ V /   | |  
 |___|_|     /_/   \_\_| |_|\__,_|_|\__, /___\___|_|       \_/    |_|  
                                    |___/                                                                        

 """)


my_file = open("iplist.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
check_list = data.split("\n")
my_file.close()


no_duplicated_check_list = list(set(check_list)) #no dublicated ips

#Determine the output txt file's name 
print("What do you want to call the 'output' file?:")
output_name = input()
output_txt = output_name + ".txt"


now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

filename = 'IPChecker-apikeys.txt'
api_keys = []

with open(filename, 'r') as f:
    for line in f:
        api_keys.append(line.strip())
    
counter = 0


# Open the output file
with open(output_txt, 'w') as f:
    # Use the values in a for loop
    
    f.write(f"Scan started at {formatted_time} \n")
    f.write("="*50 + "\n")
    
    for value in no_duplicated_check_list:
        base_url = "https://www.virustotal.com/api/v3/ip_addresses/"
        url = f"{base_url}{value}"

        headers = {
            "accept": "application/json",
            "x-apikey": api_keys[counter % len(api_keys)]
        }

        counter = counter + 1

        response = requests.get(url, headers=headers)
        json_file = json.loads(response.text)

        try:
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
        except:
            f.write("error with value="+value+"\n")
            f.write("="*50 + "\n")
            print("error with value="+value+"\n")
            print("="*50 + "\n")

print("The output is also created as " + output_txt + " in same directory. \n Press 'Enter' to exit")
x = input()
