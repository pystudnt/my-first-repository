##  This python script uses the ncclient to extract the Interface information in XML from the XRV router
#!/usr/bin/env python
from lxml import etree
from ncclient import manager
if __name__ == "__main__":
	device = manager.connect(host='xrv', port=830, username='cisco', password='cisco',
			hostkey_verify=False, device_params={'name': 'iosxr'},
			allow_agent=False, look_for_keys=False) 
	nc_filter = """
			  <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
		       <interface-configuration>
		        <interface-name>GigabitEthernet0/0/0/0</interface-name>
		       </interface-configuration>
		      </interface-configurations>
	"""
nc_get_reply = device.get(('subtree', nc_filter))
print nc_get_reply