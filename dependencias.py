from sqlalchemy.orm import sessionmaker
from modelos import db

SessionLocal = sessionmaker(bind=db)

def criar_sessao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def gerar_id_despesa(id, dataEmissao, vlrLiquido):
    chave = f"{id}_{dataEmissao}_{vlrLiquido}"
    return chave