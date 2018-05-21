# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:30:59 2018

@author: Ravi Kiran Sharma
"""

import openpyxl    ## need to import this module using pip
wb=openpyxl.load_workbook('scrutineermonk\IOC_2018_05_18.xlsx', 'r')  ## Specify the IOC workbook with Full Path
### Here I have a workbook with 5 different whorsheets named:Phishing URL's;Domains;IPs;Malicious URL's;"File Hashes
### Customize the values as pre requirment.
IOC=wb.get_sheet_names()
phishurl=wb.get_sheet_by_name("Phishing URL's")
domain=wb.get_sheet_by_name('Domains')
IP=wb.get_sheet_by_name('IPs')
malicious_url=wb.get_sheet_by_name("Malicious URL's")
hashes=wb.get_sheet_by_name("File Hashes")



import time
import json
import requests


### Take Value(a List of all IOC's and refrence set name to which bulk upload is to be done)
def ioc_update(value,ref_set_name):
    url='https://qradar.scrutineermonk.com/api/reference_data/sets/bulk_load/' ## change the "qradar.scrutineermonk.com" part woth Qradar URL
    headers={'Accept': 'application/json','SEC':'XXXXXXXXXXXXXXX','Version': '7.0', } ### Enter the api key generated from QRadar Console inplace of XXXXXXXX.
    finalurl=url+ref_set_name
#    print(finalurl)
    try:
        r = requests.post(finalurl,data=json.dumps(value),headers=headers)
#        print(r.content)
        if not r.status_code == 200:
            print("Error in Communication or Input value: \n"+"Status Code: "+str(r.status_code)+'\n'+"Input Value: "+str(value))
        else:
            print("[+] Updated")
            return
    except Exception as e:
        print("Error in Connetion "+ str(e))
        return
        
        
# Select_IOC function takes in IOC worksheet with 1st Column as IOC name eg. Domain or Phish URL and then ROW2-ROWn IOC's
# for hashes worksheet I had values in Column 2 so code will check it.

def select_ioc(IOC,RefSetName):
    IOC_title=IOC.title
#    print(str(IOC.title))
    if not IOC_title=='File Hashes':
        r='A'
    else:
        r='B'
    row_value=2
    row=r+str(row_value) ## get's the row value
    values=[]
    while True:
        try:
            ip=str(IOC[row].value)
            if ip=='None':
                break
            values.append(ip)   ### creates a list if all the IOC
            row_value = row_value + 1  ### increments the row
            row=r+str(row_value)
        except Exception as e:
            print("Error: "+str(e))
            break
#    print(str(values))
#    print(RefSetName)
    ioc_update(values,RefSetName)  ### After all the IOC's are added to list, calls the function for updating.
    return



def main():
    ref='API_PhishUrl'
    print("[-] Updating Phishing URL")
    select_ioc(phishurl,ref)
    print('==================================================================\n\n')
    time.sleep(5)
    ref='API_Domain'
    print("[-] Updating Domains")
    select_ioc(domain,ref)
    time.sleep(5)
    print('==================================================================\n\n')
    ref='API_IP'
    print("[-] Updating IP's")
    select_ioc(IP,ref)
    time.sleep(5)
    print('==================================================================\n\n')
    ref='API_MaliciousUrl'
    print("[-] Updating URL's")
    select_ioc(malicious_url,ref)
    time.sleep(5)
    print('==================================================================\n\n')
    ref='API_Hashes'
    print("[-] Updating Hashes")
    select_ioc(hashes,ref)
    print('==========================COMPLETED===============================')

    
if __name__ == "__main__":
    main()
