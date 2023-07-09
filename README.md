# Dynamic DNS script for Cloudflare domains

![](https://img.shields.io/badge/python-3.8.10-blue)
![](https://img.shields.io/github/license/jackfitton112/ddns)
![](https://img.shields.io/github/last-commit/jackfitton112/ddns)
![](https://img.shields.io/github/issues/jackfitton112/ddns)

This script will update the DNS record for a given domain with the current public IP address of the machine it is running on.

This can be used to create a dynamic DNS service for your home network if your ISP does not provide a static IP address or if you are using a VPN service.


---
## Installation

---
### Manual Installation

to install the script manually, run the following commands:


```sh
git clone https://github.com/jackfitton112/ESPCAM-Doorbell.git;
cd ESPCAM-Doorbell
```

install the required packages:

```sh
pip install -r requirements.txt
```


now create a .env file with the variables above and then run:

```sh
CF_API_KEY= YOUR_API_KEY
CF_ZONE_ID= YOUR_ZONE_ID
FETCH_INTERVAL= 300 (OPTIONAL)
```

> Fetch interval can be defined in the .env file. If not defined, file will run once and exit.

to run the script manually, run:

```sh
python3 ddns.py
```
or to run in the background:

```sh
nohup python3 ddns.py &
```

---

### Docker Installation (NOT UPDATED)

run the following command to build the docker image:
```sh
git clone https://github.com/jackfitton112/ddns.git; cd ddns
```

now create a .env file with the variables above and then run:


```shell
docker build -t ddnsimage .; docker run -d --name ddns ddnsimage
```

to run the container manually, run:

```shell
docker start ddns
```


This will run the script once and stop the container after completion. To run the script on a schedule, add the following line to your crontab:

```sh
*/5 * * * * docker start ddns
```

#### Please feel free to submit any issues or pull requests if you have any suggestions or improvements.

