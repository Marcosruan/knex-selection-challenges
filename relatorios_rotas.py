from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from modelos import Despesa, Deputado
from dependencias import criar_sessao

relatorios_roteador = APIRouter(prefix="/relatorios", tags=["Relatórios"])

@relatorios_roteador.get("/deputados/{deputado_id}/total-despesas")
async def total_despesas_por_deputado(deputado_id: int, sessao: Session = Depends(criar_sessao)):
    deputado = sessao.query(Deputado).filter(Deputado.id == deputado_id).first()
    if not deputado:
        raise HTTPException(status_code=400, detail="Deputado não encontrado")

    total = sessao.query(func.sum(Despesa.valorLiquido)).filter(Despesa.deputado_id == deputado_id).scalar()

    return {
        "deputado": deputado.nome,
        "uf": deputado.uf,
        "partido": deputado.partido,
        "total_despesas": round(total, 2)
    }

@relatorios_roteador.get("/total-despesas")
async def total_geral(sessao: Session = Depends(criar_sessao)):
    total = sessao.query(func.sum(Despesa.valorLiquido)).scalar()
    return {"Total de despesas de todos os deputados": round(total or 0.0, 2)}