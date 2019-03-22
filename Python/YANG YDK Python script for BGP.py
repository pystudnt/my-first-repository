#  Python script to use YDK Yang tools to edit BGP
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.openconfig import bgp

if __name__ == "__main__":

	provider = NetconfServiceProvider (address= 'xrv',
							port = 830,
							username="cisco",
							password="cisco",
							protcol="ssh")
	crud = CRUDService()
	bgp = bgp.Bgp()
	bgp.global_.config.as_ = 65000
	bgp.global_config.router_id = '10.1.1.1'
	crud.create(provider, bgp)
	provider.close()
