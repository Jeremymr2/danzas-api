from sqlalchemy import Column, Integer, String, Date, Text

from .database import Base

class Expresion(Base):
    __tablename__ = "expresiones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    resolucion = Column(String(255))
    clasificacion = Column(String(255))
    expresion = Column(String(255))
    contenido = Column(Text)
    departamento = Column(String(255))
    provincia = Column(String(255))
    distrito = Column(String(255))