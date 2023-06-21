# Dynamic DNS Script for Cloudflare domains

This script will update the DNS record for a given domain with the current public IP address of the machine it is running on.

This can be used to create a dynamic DNS service for your home network if your ISP does not provide a static IP address or if you are using a VPN service.

---
## Requirements

* Python 3
* Cloudflare account
* Cloudflare API key
* Cloudflare zone ID for the domain you want to update
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
---
## __This is currently under development and is very inefficient, please use the manual installation for now.__
---
> Dockerfile has currently been deleted as it is not working correctly. I will update this when I have fixed it.

run the following command to build the docker image:
```sh
git clone https://github.com/jackfitton112/ddns.git; cd ddns

```

now create a .env file with the variables above and then run:

```sh
You need to create the .env file in the same directory as the script with the following variables:

```shell

docker build -t ddnsimage .; docker run -d --name ddns ddnsimage

```




This will run the script once and stop the container after completion. To run the script on a schedule, add the following line to your crontab:

```sh
*/5 * * * * docker start ddns
```

#### Please feel free to submit any issues or pull requests if you have any suggestions or improvements.

