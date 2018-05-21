###  POST
import requests
import json
url='https://qradar.scrutineermonk.com/api/reference_data/sets/' ## change the "qradar.scrutineermonk.com" part with Qradar URL
headers={'Accept': 'application/json','SEC':'XXXXXXXXXXXXX','Version': '7.0', }  ### Enter the api key generated from QRadar Console inplace of XXXXXXXX.
referense_set='API_Test'
value='TEST'
value1='value='+value
finalurl=url+referense_set+'?'+value1
print(finalurl)
r = requests.post(finalurl,headers=headers)
#print(r.content)
print(r.status_code)
print(r.json())


### GET
url='https://qradar.scrutineermonk.com/api/reference_data/sets/'
headers={'Accept': 'application/json','SEC':'XXXXXXXXXXXXX','Version': '7.0', }  ### Enter the api key generated from QRadar Console inplace of XXXXXXXX.
referense_set='API_Test'
finalurl=url+referense_set
print(finalurl)
r = requests.get('qradar.scrutineermonk.com/api/reference_data/sets/API_Test',headers=headers)
#b=r.content
b=r.json()
print(b)
print(r.status_code)


#### Bulk Upload To Reference Set
url='https://qradar.scrutineermonk.com/api/reference_data/sets/bulk_load/'
headers={'Accept': 'application/json','SEC':'XXXXXXXXXXXXX','Version': '7.0', }  ### Enter the api key generated from QRadar Console inplace of XXXXXXXX.
referense_set='API_Test'
data=['37.48.65.143', '109.201.133.68', '162.210.195.122', '162.222.213.199', '45.77.226.209', '95.211.244.75', '45.77.226.209']
jsondump=json.dumps(data)
print(type(jsondump))
finalurl=url+referense_set
print(finalurl)
#r = requests.post('qradar.scrutineermonk.com/api/reference_data/sets/bulk_load/API_Test',data=json.dumps(data),headers=headers)
r = requests.post(finalurl,data=json.dumps(data),headers=headers)
print(r.status_code)
print(r.content)
