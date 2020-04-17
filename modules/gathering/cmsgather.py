import requests
import re
from common.colors import G,W
def drupal_version(url,headers):
    response = requests.get(url, headers).text
    try:
        matches = re.compile(r'Drupal \d{0,10}').findall(response)
        if len(matches) > 0 and matches[0] != None and matches[0] != "":
            version = matches[0]
            print('%s [+] Drupal Version : %s %s' % (G, version, W))
    except Exception as error_:
        print('Handling Error : ' + str(error_))

# Prestashop Version


def prestashop_version(url,headers):
    response = requests.get(url, headers).text
    try:
        matches = re.compile(r'Prestashop \d{0,9}').findall(response.text)
        if len(matches) > 0 and matches[0] != None and matches[0] != "":
            version = matches[0]
            return print('%s [+] Prestashop Version : %s %s' % (G, version, W))
    except Exception as error_:
        print('Handling Error : ' + str(error_))
