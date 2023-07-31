from infrastructure.config.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Float

class Network(Base):
    __tablename__ = 'networks'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    host = Column(String(255))
    provider = Column(String(255))
    local_provider = Column(String(255))
    download = Column(Float)
    upload = Column(Float)
    latency = Column(Float)
    deleted_at = Column(DateTime)
    
    def __repr__(self):
        return f'<Network (created={self.created}, host={self.host}, provider={self.provider}, local_provider={self.local_provider}, download={self.download}, upload={self.upload}, latency={self.latency})>'


