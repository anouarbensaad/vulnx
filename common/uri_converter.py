import re

def convert_uri(url):
    urlform = r'(https?://)(www\.)?((\w+)[a-zA-Z0-9-_.]?[a-zA-Z0-9-_.]?[a-zA-Z0-9-_.]?\.\w+)'
    domain = re.search(urlform,url)
    return domain.group(3)
