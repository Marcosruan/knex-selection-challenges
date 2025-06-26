from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from modelos import Deputado
from dependencias import criar_sessao


deputados_roteador = APIRouter(prefix="/deputados", tags=["Deputados"])

@deputados_roteador.get("")
async def listar_deputados(uf: str = Query(None, description="Sigla da Unidade Federativa"), sessao: Session = Depends(criar_sessao)):
    if uf:
        uf = uf.upper()
        buscador = sessao.query(Deputado).filter(Deputado.uf == uf)
        if not sessao.query(Deputado).filter(Deputado.uf == uf).first():
            raise HTTPException(status_code=400, detail=f"UF '{uf}' não encontrada no banco de dados.")

    deputados = buscador.all()

    return [
        {
            "id": dado.id,
            "nome": dado.nome,
            "uf": dado.uf,
            "cpf": dado.cpf,
            "partido": dado.partido
        } for dado in deputados
    ]