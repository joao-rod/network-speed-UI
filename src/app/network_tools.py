from speedtest import Speedtest

class Conection_Test:
    def __init__(self):
        self.st = Speedtest()
        self.st.get_servers()
        self.server = self.st.get_best_server()
        
        self.download = None
        self.upload = None
        self.provider = None
        self.local_provider = None
        self.host = None
        self.latency = None

    def test_conection(self): 
        self.download = round(self.st.download() / (1024 * 1024), 2)
        self.upload = round(self.st.upload() / (1024 * 1024), 2)
        self.provider = self.server["sponsor"]
        self.local_provider = f'{self.server["name"]}/{self.server["cc"]}'
        self.host = self.server["host"]
        self.latency = round(self.server["latency"], 2)

