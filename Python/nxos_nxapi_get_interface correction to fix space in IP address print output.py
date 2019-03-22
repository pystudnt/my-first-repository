#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show interface mgmt0",
            "output_format": "json"
        }
    }
    url = 'http://nxosv/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

    #print 'Status Code: ' + str(response.status_code)
    rx_object = json.loads(response.text)
    #print json.dumps(rx_object, indent=4)

    robj = rx_object['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
    #print robj

    print "Management Interface Information:"

    # Lines 39-42: curly braces are replaced by 'format()' arguments; this 
    # removes unwanted extra spaces in the output
    print ("IP Address:  {}/{}".format(robj['eth_ip_addr'], robj['eth_ip_mask']))
    print ("Speed:       {}".format(robj['eth_speed']))
    print ("State:       {}".format(robj['state']))
    print ("MTU:         {}".format(robj['eth_mtu']))

