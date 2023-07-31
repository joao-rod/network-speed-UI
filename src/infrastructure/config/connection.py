from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
    
    def __init__(self) -> None:
        self.__BASEURL = 'mysql+pymysql://phpmyadmin:root@localhost/net_speed'
        self.__engine = self.__create_db_engine()
        self.session = None
        
    def __create_db_engine(self):
        engine = create_engine(self.__BASEURL)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        
                