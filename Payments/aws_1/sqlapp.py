from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

#mysql+pymysql://lldlt:Luislerma1996$@bedu-llt-2101.cqoiqc8blzss.us-east-2.rds.amazonaws.com/python_db

engine = create_engine('mysql+pymysql://lldlt:Luislerma1996$@bedu-llt-2101.cqoiqc8blzss.us-east-2.rds.amazonaws.com/python_db')
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable = False, unique = True)
    email = Column(String(50), nullable = False, unique = True)
    created_at = Column(DateTime(), default = datetime.now())
    
    def __str__(self):
        return self.username

#Class
Session = sessionmaker(engine) 

#Instance
session = Session()

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    user1 = User(username="User1", email="example1@ex.com")
    user2 = User(username="User2", email="example2@ex.com")
    user3 = User(username="User3", email="example3@ex.com")

    session.add(user1)
    session.add(user2)
    session.add(user3)

    session.commit()