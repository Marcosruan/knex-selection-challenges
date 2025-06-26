from fastapi import FastAPI 
app = FastAPI()
from upload_ceap_rotas import upload_ceap_roteador 
from despesas_rotas import despesas_roteador 
from relatorios_rotas import relatorios_roteador 
from deputados_rotas import deputados_roteador 

app.include_router(relatorios_roteador)
app.include_router(despesas_roteador)
app.include_router(upload_ceap_roteador)
app.include_router(deputados_roteador)
