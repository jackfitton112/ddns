# Dynamic DNS script for Cloudflare domains

![](https://img.shields.io/badge/python-3.8.10-blue)
![](https://img.shields.io/github/license/jackfitton112/ddns)
![](https://img.shields.io/github/last-commit/jackfitton112/ddns)
![](https://img.shields.io/github/issues/jackfitton112/ddns)

This script will update the DNS record for a given domain with the current public IP address of the machine it is running on.

This can be used to create a dynamic DNS service for your home network if your ISP does not provide a static IP address or if you are using a VPN service.


---
## Installation

Make sure you have created a .env file in the same directory as the script with the following variables:

```shell
CF_API_KEY= YOUR_API_KEY
CF_ZONE_ID= YOUR_ZONE_ID
```

---
### Manual Installation

- This script is designed to run in cron, so clone the repo to a location of your choice and add the following line to your crontab:

```sh
*/5 * * * * /path/to/script/ddns.py
```
> This will run the script every 5 minutes. You can change this to whatever interval you want.

---

### Docker Installation

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

