from datetime import datetime
from infrastructure.entities.network import Network
from infrastructure.repository.network_repository import NetworkRepository

network = Network()
data = NetworkRepository()

network.created = datetime.now()
network.host = 'host'
network.provider = 'provider'
network.local_provider = 'local_provider'
network.download = 10.5
network.upload = 9.001
network.latency = 0.001

data.insert(network)
# data.delete(1)

print(data.get_all())