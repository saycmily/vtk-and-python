import re

def validIPAddress(IP):
    if not IP:
        return "Neither"
    
    regex0 = r"\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]"
    regexIPv4 = regex0 + "(\\." + regex0 + "){3}"
    regex1 = r"[\da-fA-F]{1,4}"
    regexIPv6 = regex1 + "(:" + regex1 + "){7}"
    result = "Neither"
    if re.match(regexIPv4, IP):
        result = "IPv4"
    elif re.match(regexIPv6, IP):
        a = re.match(regexIPv6, IP)
        print(a.group(0))
        print(len(a.groups()))
        
        result = "IPv6"
    
    
    return result

a = validIPAddress("172.16.254.1")
print(a)

