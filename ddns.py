import json, time, os, asyncio, aiohttp
from dotenv import load_dotenv

def load_from_dotenv():

        #load .env file
        load_dotenv()

        #set global variables
        global CF_API_KEY
        global CF_ZONE_ID
        global FETCH_INTERVAL

        #get API Key and Zone ID from .env file
        CF_API_KEY = os.getenv("CF_API_KEY")
        CF_ZONE_ID = os.getenv("CF_ZONE_ID")
        FETCH_INTERVAL = os.getenv("FETCH_INTERVAL")

        #if the vars are not set exit with error
        if CF_API_KEY is None or CF_ZONE_ID is None:
                assert False, "CF_API_KEY or CF_ZONE_ID is not set"
        
        #if file is loaded return true
        return True

#load .env file
load_from_dotenv()

async def getIP() -> str:
        res = await aiohttp.request('GET', 'https://api.ipify.org?format=json')
        response = json.loads(res.text)
        return response['ip']

async def TestAPI() -> bool:
        # Test API and Validate API Key using /verify endpoint
        url = "https://api.cloudflare.com/client/v4/user/tokens/verify"

        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }
        #make async request test API
        x = await aiohttp.request('GET', url, headers = headers)
        response = json.loads(x.text)
        try:
                if response['result']['status'] == "active":
                        return True
        except:
                return False

async def getDomainDNSRecords():

        url = f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/dns_records/"

        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }

        response = await aiohttp.request('GET', url, headers = headers)
        data = json.loads(response.text)
        print(data)
        try:
                array = {"ip":data['result'][0]['content'], "id":data['result'][0]['id']}
                return (array)
        except:
                return False

async def updateDomainDNSRecords(aRecord) -> bool:

        url = f"https://api.cloudflare.com/client/v4/zones/{CF_ZONE_ID}/dns_records/{aRecord}"


        headers = {
               'Authorization':f'Bearer {CF_API_KEY}',
               'Content-Type':'application/json'
        }

        #data to be sent to api to update A record with current IP
        data = {"type":"A","name":"@","content":getIP(),"ttl":1,"proxied":False}
        response = await aiohttp.request('PUT', url, headers = headers, data = json.dumps(data))

        #if response is successful return true
        try:
                if response['success'] == True:
                        return True
        except:
                return False

async def main():


        #Test API Key
        if await TestAPI() == False:
                assert False, "API Key is not valid"

        #Get the current IP from A record
        aRecord = await getDomainDNSRecords()["ip"]

        #get current IP
        currentIP = await getIP()

        #if current IP is not equal to A record IP update A record
        if currentIP != aRecord:

                #update A record, if not successful exit with error
                if not(await updateDomainDNSRecords(getDomainDNSRecords()["id"])):
                        assert False, "Unable to update A record"

        return True

async def runner():

        if FETCH_INTERVAL is None:
                await main()
        else:
                while True:
                        await asyncio.run(main())
                        await asyncio.sleep(int(FETCH_INTERVAL))


asyncio.run(runner())