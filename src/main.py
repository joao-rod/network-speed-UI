from datetime import datetime
from app.network_tools import Conection_Test
from infrastructure.entities.network import Network
from infrastructure.repository.network_repository import NetworkRepository

conection = Conection_Test()
conection.test_conection()

network = Network(
    created_at = datetime.now(),
    download = conection.download,
    upload = conection.upload,
    provider = conection.provider,
    local_provider = conection.local_provider,
    host = conection.host,
    latency = conection.latency,
    deleted_at = None
)

data = NetworkRepository()
data.insert(network)