import requests
import json
from dotenv import load_dotenv
import os

#load .env file
load_dotenv()
try:
        CF_API_KEY = os.getenv("CF_API_KEY")
        CF_ZONE_ID = os.getenv("CF_ZONE_ID")
except:
        print("Error loading .env file")
        exit(2)

def getIP():
        res = requests.get("https://api.ipify.org?format=json")
        response = json.loads(res.text)
        return response['ip']

def TestAPI():
        # Test API and Validate API Key using /verify endpoint
        url = "https://api.cloudflare.com/client/v4/user/tokens/verify"

        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }

        x = requests.get(url, headers = headers)
        response = json.loads(x.text)
        if response['result']['status'] == "active":
                return True
        else:
                return False

def getDomainDNSRecords():

        url = f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/dns_records/"

        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }

        response = requests.get(url, headers = headers)
        data = json.loads(response.text)
        array = {"ip":data['result'][0]['content'], "id":data['result'][0]['id']}
        return (array)

def updateDomainDNSRecords(aRecord):

        url = f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/dns_records/{aRecord}"


        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }

        #data to be sent to api to update A record with current IP
        data = {"type":"A","name":"@","content":getIP(),"ttl":1,"proxied":False}
        response = requests.put(url, headers = headers, data = json.dumps(data))

        #if response is successful return true
        if response['success'] == True:
                return True
        else:
                return False

# Check the API is working with the API key
if TestAPI():

        #get the IP address of the device (Ext IPv4 Address)
        deviceIP = getIP()

        #get the IP address of the A record for the domain
        SiteArray = getDomainDNSRecords()

        #assign vars for the site IP and the site ID
        SiteIP = SiteArray['ip']
        SiteID = SiteArray['id']
        if deviceIP == SiteIP:
            exit(0)
        else:

            if updateDomainDNSRecords(SiteID):
                exit(0)
            else:
                #exit with code 3 if update fails for reason other than API
                exit(3)

else:
        # API Key is not valid or API is down
        exit(1)