from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, Date
from sqlalchemy.orm import sessionmaker

#mysql+pymysql://lldlt:Luislerma1996$@bedu-llt-2101.cqoiqc8blzss.us-east-2.rds.amazonaws.com/python_db

engine = create_engine('mysql+pymysql://root@localhost/python_db2')
Base = declarative_base()

class Pay(Base):
    __tablename__ = "payments"
    
    id_pago = Column(Integer(), primary_key=True)
    id_contrato = Column(Integer())
    id_cliente = Column(Integer())
    fecha = Column(Date())
    monto = Column(Float())
    activo = Column(Boolean())
    fecha_registro = Column(DateTime(), default = datetime.now())
    
    def __str__(self):
        return self.id_cliente

#Class
Session = sessionmaker(engine) 

#Instance
session = Session()

if __name__ == "__main__":
 
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    pay1 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-01-10", monto = 10000, activo = True)
    pay2 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-02-10", monto = 10000, activo = True)
    pay3 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-03-10", monto = 10000, activo = True)
    pay4 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-04-10", monto = 10000, activo = True)
    pay5 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-05-10", monto = 10000, activo = True)
    pay6 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-06-10", monto = 10000, activo = True)
    pay7 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-07-10", monto = 10000, activo = True)
    pay8 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-08-10", monto = 10000, activo = True)
    pay9 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-09-10", monto = 10000, activo = True)
    pay10 = Pay(id_contrato = 1, id_cliente = 1, fecha = "2021-10-10", monto = 10000, activo = True)

    session.add(pay1)
    session.add(pay2)
    session.add(pay3)
    session.add(pay4)
    session.add(pay5)
    session.add(pay6)
    session.add(pay7)
    session.add(pay8)
    session.add(pay9)
    session.add(pay10)

    session.commit()