from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base
import os

db = create_engine(os.getenv("DATABASE_URL"))

Base = declarative_base() 

class Deputado(Base):
    __tablename__ = "Deputados"
    id = Column("id", Integer, primary_key=True, index=True)
    nome = Column("nome", String, nullable=False)
    uf = Column("uf", String, nullable=False)
    cpf = Column("cpf", String, unique=False)
    partido = Column("partido", String)

    def __init__(self, id, nome, uf, cpf, partido):
        self.id = id
        self.nome = nome
        self.uf = uf
        self.cpf = cpf
        self.partido = partido
    
class Despesa(Base):
    __tablename__ = "Despesas"
    id = Column("id", String, primary_key=True)
    dataEmissao = Column("dataEmissao", String) 
    fornecedor = Column("fornecedor", String)
    valorLiquido = Column("valorLiquido", Float)
    deputado_id = Column("deputado_id", ForeignKey('Deputados.id'))
    urlDocumento =  Column("urlDocumento", String, default=None)


    def __init__(self, id, dataEmissao, fornecedor, valorLiquido, deputado_id, urlDocumento = None):
        self.id = id
        self.dataEmissao = dataEmissao
        self.fornecedor = fornecedor
        self.valorLiquido = valorLiquido
        self.deputado_id = deputado_id
        self.urlDocumento = urlDocumento