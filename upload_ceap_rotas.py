from fastapi import APIRouter, UploadFile, Depends, HTTPException
import pandas as pd
from modelos import Deputado, Despesa
from dependencias import criar_sessao, gerar_id_despesa
from sqlalchemy.orm import Session


upload_ceap_roteador = APIRouter(prefix="/upload_ceap", tags=["Upload_ceap"])
@upload_ceap_roteador.post("")
async def upload_ceap(arquivo: UploadFile, sessao: Session = Depends(criar_sessao)):
    try:
        df = pd.read_csv(arquivo.file, sep=';')
        df = df[df['sgUF'].notna()]
        cont_nova_entrada = cont_existente = 0

        for linha in df.itertuples(index=False):
            deputado_id = sessao.query(Deputado).filter(Deputado.id==linha.ideCadastro).first()
            if not deputado_id:
                cont_nova_entrada += 1
                deputado = Deputado(linha.ideCadastro, linha.txNomeParlamentar, linha.sgUF, linha.cpf, linha.sgPartido)
                sessao.add(deputado)
                sessao.commit()
            else:
                cont_existente +=1
            
            hash_despesa = gerar_id_despesa(linha.ideCadastro, linha.datEmissao, linha.vlrLiquido)
            despesa_id = sessao.query(Despesa).filter(Despesa.id==hash_despesa).first()
            if not despesa_id:
                despesa = Despesa(hash_despesa, linha.datEmissao, linha.txtFornecedor, linha.vlrLiquido, linha.ideCadastro, linha.urlDocumento)
                sessao.add(despesa)
                sessao.commit()

        if cont_nova_entrada == 0:
            raise HTTPException(status_code=400, detail="Todos os dados já existem no banco!")
        else:
            return {"mensagem": "Dados adicionados com sucesso"}


    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    