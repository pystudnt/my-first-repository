#   Note that this script expects HTTP port 80 on the APIC, which is off by default. 
# 	To enable HTTP in the APIC, navigate to FABRIC, FABRIC POLICIES Pod Policies     Policies   Management Acces    default  then enable HTTP
import requests
import json

def get_cookies(apic):
	username = 'admin'
	password = 'cisco123'
	url = apic + '/api/aaaLogin.json'
	auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
	authenticate = requests.post(url, data=json.dumps(auth), verify=False)
	return authenticate.cookies
	
def add_tenant(apic,cookies):
	jsondata = {"fvTenant":{"attributes":{"dn":"uni/tn-Procurement","name":"Procurement","rn":"tn-Procurement","status":"created"},"children":[]}}
	result = requests.post('{0}://{1}/api/node/mo/uni/tn-Procurement.json'.format(protocol,host), cookies=cookies, data=json.dumps(jsondata), verify=False)
	print result.status_code
	print result.text

def get_tenants(apic,cookies):
	uri = '/api/class/fvTenant.json'
	url = apic + uri
	req = requests.get(url, cookies=cookies, verify=False)
	response = req.text
	return response

if __name__ == "__main__":
	protocol = 'http'
	host = 'apic'
	apic = '{0}://{1}'.format(protocol, host)
	cookies = get_cookies(apic)
	add_tenant(apic,cookies)
	rsp = get_tenants(apic,cookies)
	
rsp_dict = json.loads(rsp)
tenants = rsp_dict['imdata']
	
for tenant in tenants:
	print tenant['fvTenant']['attributes']['name']