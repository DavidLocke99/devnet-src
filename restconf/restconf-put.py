import json
import requests
requests.packages.urllib3.disable_warnings()

api_url="https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
headers={
    "Accept": "application/yang-data+json", 
    "Content-type":"application/yang-data+json"
}
basicauth=("cisco", "cisco123!")

yangConfig={
    "ietf-interfaces:interfaces": {
        "name": "Loopback2",
        "description": "My second restconf loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code>= 200 and resp.status_code<=299):
    print("STATUS OKAY:{}".format(resp.status_code))
else:
    print('Error. Status Code:{} \nError message:{}'.format(resp.status_code, resp.json()))

