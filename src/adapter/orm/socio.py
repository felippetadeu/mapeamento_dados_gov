from sqlalchemy import Column, Integer, String
from src.adapter.orm.base import Base

class Socio(Base):
    __tablename__ = 'socios'
    cnpj_basico = Column(String, primary_key=True)
    identificador_socio = Column(Integer, primary_key=True)
    nome_socio = Column(String)
    cnpj_cpf_socio = Column(String)
    qualificacao_socio = Column(Integer)
    data_entrada_sociedade = Column(String)
    pais = Column(String)
    representante_legal = Column(String)
    nome_representante = Column(String)
    qualificacao_representante_legal = Column(Integer)
    faixa_etaria = Column(Integer)
