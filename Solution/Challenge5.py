#  Python for Network Engineers Challenge Lab #5 Solution
#  Revision May 22 2018

# Requests module required to be loaded first for REST
import requests

#  URL for Cisco UCS RESTful Interface:

url = "http://192.168.10.90/nuova"

#  XML Payload to create the Service Profile named Linux

payload = "<configConfMos\r\ncookie=\"1526582583/277ed050-a86a-45b0-a46b-e96d0f9fb280\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Linux\">\r\n    <lsServer\r\n    name=\"Linux\"\r\n    dn=\"org-root/ls-Linux\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth0\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"ether-eth0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"finance\"\r\n            \r\n            rn=\"if-finance\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth1\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"ether-eth1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"finance\"\r\n            \r\n            rn=\"if-finance\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc0\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"fc-fc0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc1\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"fc-fc1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <lsbootDef\r\n        \r\n        rn=\"boot-policy\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <lsbootStorage\r\n            order=\"1\"\r\n            \r\n            rn=\"storage\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n                <lsbootLocalStorage\r\n                \r\n                rn=\"local-storage\"\r\n                \r\n                \r\n                sacl=\"addchild,del,mod\">\r\n                    <lsbootDefaultLocalImage\r\n                    order=\"1\"\r\n                    \r\n                    rn=\"local-any\"\r\n                    \r\n                    \r\n                    sacl=\"addchild,del,mod\">\r\n                    </lsbootDefaultLocalImage>\r\n                </lsbootLocalStorage>\r\n            </lsbootStorage>\r\n        </lsbootDef>\r\n        <vnicFcNode\r\n        addr=\"pool-derived\"\r\n        identPoolName=\"\"\r\n        \r\n        rn=\"fc-node\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFcNode>\r\n    </lsServer>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# Manually add VSAN 10 for fabric A to the Linux Service Profile

payload = "<configConfMos\r\ncookie=\"1526594605/c9a84c9a-8a4d-494e-a7b7-ca99f98cc52b\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Linux/fc-fc0/if-default\">\r\n    <vnicFcIf\r\n    name=\"VSAN10\"\r\n    dn=\"org-root/ls-Linux/fc-fc0/if-default\"\r\n    \r\n    status=\"created,modified\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </vnicFcIf>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

#  Manually add VASN 11 for fabric B to the Linux Service Profile

payload = "<configConfMos\r\ncookie=\"1526595210/c8ba34ba-2d62-43b2-8413-a1cef122ba6b\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Linux/fc-fc1/if-default\">\r\n    <vnicFcIf\r\n    name=\"VSAN11\"\r\n    dn=\"org-root/ls-Linux/fc-fc1/if-default\"\r\n    \r\n    status=\"created,modified\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </vnicFcIf>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

#  XML Payload to create Exchange Service Profile

payload = "<configConfMos\r\ncookie=\"1526593393/63f78584-6ff4-4888-aa6d-d2429f6164cb\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Exchange\">\r\n    <lsServer\r\n    name=\"Exchange\"\r\n    dn=\"org-root/ls-Exchange\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth0\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"ether-eth0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"human-resource\"\r\n            \r\n            rn=\"if-human-resource\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicEther\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        mtu=\"1500\"\r\n        name=\"eth1\"\r\n        nwCtrlPolicyName=\"\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"ether-eth1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <vnicEtherIf\r\n            defaultNet=\"yes\"\r\n            name=\"human-resource\"\r\n            \r\n            rn=\"if-human-resource\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n            </vnicEtherIf>\r\n        </vnicEther>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc0\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"A\"\r\n        \r\n        rn=\"fc-fc0\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <vnicFc\r\n        adaptorProfileName=\"\"\r\n        addr=\"derived\"\r\n        adminCdnName=\"\"\r\n        adminHostPort=\"ANY\"\r\n        adminVcon=\"any\"\r\n        cdnPropInSync=\"yes\"\r\n        cdnSource=\"vnic-name\"\r\n        identPoolName=\"\"\r\n        maxDataFieldSize=\"2048\"\r\n        name=\"fc1\"\r\n        nwTemplName=\"\"\r\n        order=\"unspecified\"\r\n        persBind=\"disabled\"\r\n        persBindClear=\"no\"\r\n        pinToGroupName=\"\"\r\n        qosPolicyName=\"\"\r\n        statsPolicyName=\"default\"\r\n        switchId=\"B\"\r\n        \r\n        rn=\"fc-fc1\"\r\n        status=\"created\"\r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFc>\r\n        <lsbootDef\r\n        \r\n        rn=\"boot-policy\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n            <lsbootStorage\r\n            order=\"1\"\r\n            \r\n            rn=\"storage\"\r\n            \r\n            \r\n            sacl=\"addchild,del,mod\">\r\n                <lsbootLocalStorage\r\n                \r\n                rn=\"local-storage\"\r\n                \r\n                \r\n                sacl=\"addchild,del,mod\">\r\n                    <lsbootDefaultLocalImage\r\n                    order=\"1\"\r\n                    \r\n                    rn=\"local-any\"\r\n                    \r\n                    \r\n                    sacl=\"addchild,del,mod\">\r\n                    </lsbootDefaultLocalImage>\r\n                </lsbootLocalStorage>\r\n            </lsbootStorage>\r\n        </lsbootDef>\r\n        <vnicFcNode\r\n        addr=\"pool-derived\"\r\n        identPoolName=\"\"\r\n        \r\n        rn=\"fc-node\"\r\n        \r\n        \r\n        sacl=\"addchild,del,mod\">\r\n        </vnicFcNode>\r\n    </lsServer>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# Manually add VSAN 10 for fabric A to the Exchange Service Profile

payload = "<configConfMos\r\ncookie=\"1526595210/c8ba34ba-2d62-43b2-8413-a1cef122ba6b\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Exchange/fc-fc0/if-default\">\r\n    <vnicFcIf\r\n    name=\"VSAN10\"\r\n    dn=\"org-root/ls-Exchange/fc-fc0/if-default\"\r\n    \r\n    status=\"created,modified\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </vnicFcIf>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

# Manually add VSAN 11 for fabric B to the Exchange Service Profile

payload = "<configConfMos\r\ncookie=\"1526595210/c8ba34ba-2d62-43b2-8413-a1cef122ba6b\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/ls-Exchange/fc-fc1/if-default\">\r\n    <vnicFcIf\r\n    name=\"VSAN11\"\r\n    dn=\"org-root/ls-Exchange/fc-fc1/if-default\"\r\n    \r\n    status=\"created,modified\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </vnicFcIf>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
