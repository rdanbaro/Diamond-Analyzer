from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Sprint(Base):
    __tablename__ = 'Sprints'

    id = Column(Integer(), primary_key=True)
    nombre_sprint = Column(String(45), nullable=False, unique=True)
    tipo = Column(String(45), nullable=False)
    data_metas_objetivos = Column(String(100), nullable=False)
    data_Habitos = Column(String(100))
    data_Entrenamiento = Column(String(100))
    data_Diamantes = Column(String(100))