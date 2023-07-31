from infrastructure.entities.network import Network
from infrastructure.config.connection import DBConnection

class NetworkRepository():
    def get_all(self):
        with DBConnection() as db:
            networks = db.session.query(Network).all()
            return networks
        
    def insert(self, network):
        with DBConnection() as db:
            db.session.add(network)
            db.session.commit()
        
    def update(self, id):
        with DBConnection() as db:
            db.session.query(Network).filter(Network.id == id).update(id)
            db.session.commit()

    def delete(self, id):
        with DBConnection() as db:
            db.session.query(Network).filter(Network.id == id).delete()
            db.session.commit()