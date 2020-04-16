import requests
import re

url = "http://helloktebi.com/"
header = {
    "content-type" : "*/*",
    "accept": "*/*"
}
response = requests.get(url,headers=header).headers
server_response = response["server"]
regx = re.compile(r"(.+) \((.+)\)")
find = regx.search(server_response)
print(find.group(2))
