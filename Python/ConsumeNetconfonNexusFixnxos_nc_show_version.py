#!/usr/bin/env python

from ncclient import manager

# Added function to remove namspaces
def remove_namespaces(xml):
	for elem in xml.getiterator():
		split_tag = elem.tag.split('}')
		if len(split_tag) > 1:
			elem.tag = split_tag[1]
	return xml
	
if __name__ == '__main__':

	with manager.connect(host='nxosv', port=22, username='cisco', password='cisco',
						hostkey_verify=False, device_params={'name': 'nexus'},
						allow_agent=False, look_for_keys=False) as device:
						
		get_filter = """
					<show>
						<version>
						</version>
					</show>
					"""
		nc_get_reply = device.get(('subtree', get_filter))
		# Added a no namespace variable
		nc_get_reply_no_ns = remove_namespaces(nc_get_reply.data_ele)
		print 'Response as XML String: '
		print nc_get_reply.xml
		
		# no longer using namespaces for this
		# ns_map = {'mod': 'http://www.cisco.com/nxos:1.0:vdc_mgr'}
		# modified the original lookup/find
		# xml_rsp_cid = nc_get_reply.data_ele.find('//mod:chassis_id', ns_map)
		xml_rsp_cid = nc_get_reply_no_ns.find('.//chassis_id')
		cid_value = xml_rsp_cid.text
		# modified the original lookup/find
		# xml_rsp_sw = nc_get_reply.data_ele.find('//mod:sys_ver_str', ns_map)
		xml_rsp_sw = nc_get_reply_no_ns.find('.//sys_ver_str')
		sw_value = xml_rsp_sw.text
		print '================================'
		print 'Chassis ID: ', cid_value
		print 'Software Version: ', sw_value