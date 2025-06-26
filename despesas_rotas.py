from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from modelos import Despesa
from dependencias import criar_sessao

despesas_roteador = APIRouter(prefix="/despesas", tags=["Despesas"])
@despesas_roteador.get('')
async def listar_despesas(limit: int = Query(10, description="Quantidade de despesas retornadas"), 
                    offset: int = Query(0, description="Quantidade de despesas puladas"),
                    session: Session = Depends(criar_sessao)):
    dados_despesas = session.query(Despesa).offset(offset).limit(limit).all()

    return [
        {
            "Data de emissão": dado.dataEmissao,
            "fornecedor": dado.fornecedor,
            "Valor liquido": dado.valorLiquido,
            "URL do documento": dado.urlDocumento,
        } for dado in dados_despesas
    ]