import requests
import json
from dotenv import load_dotenv
import os

#load .env file and get API Key and Zone ID
load_dotenv()

try:
        CF_API_KEY = os.getenv("CF_API_KEY")
        CF_ZONE_ID = os.getenv("CF_ZONE_ID")
except:
        #print("Error loading .env file")
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
        try:
                if response['result']['status'] == "active":
                        return True
        except:
                return False

def getDomainDNSRecords():

        url = f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/dns_records/"

        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }

        response = requests.get(url, headers = headers)
        data = json.loads(response.text)
        print(data)
        try:
                array = {"ip":data['result'][0]['content'], "id":data['result'][0]['id']}
                return (array)
        except:
                return False

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
        try:
                if response['success'] == True:
                        return True
        except:
                return False

def main():

        #Test API Key
        if TestAPI() == False:
                #print("Invalid API Key")
                exit(2)

        #Get the current IP from A record
        aRecord = getDomainDNSRecords()["ip"]

        #get current IP
        currentIP = getIP()

        #if current IP is not equal to A record IP update A record
        if currentIP == aRecord:
                #print("IP is the same")
                exit(0)

        #update A record
        if updateDomainDNSRecords(getDomainDNSRecords()["id"]) == True:
                #print("A Record Updated")
                exit(0)
        else:
                #print("Error Updating A Record")
                exit(2)



#call main function
main()