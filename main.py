from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import logging

app = FastAPI()

# URL definitiva (produção) do n8n
N8N_WEBHOOK_URL = "https://agroseguro.app.n8n.cloud/webhook/salvar-dados-nf"

# Configura logs no console do Render
logging.basicConfig(level=logging.INFO)

@app.post("/receber-analise")
async def receber_analise(request: Request):
    try:
        dados = await request.json()
        logging.info("📥 Dados recebidos do Assistente:")
        logging.info(dados)

        # Encaminha os dados para o n8n
        resposta_n8n = requests.post(N8N_WEBHOOK_URL, json=dados)
        logging.info("📤 Enviado ao n8n:")
        logging.info(resposta_n8n.status_code)
        logging.info(resposta_n8n.text)

        return JSONResponse(content={
            "mensagem": "Dados recebidos e encaminhados ao n8n com sucesso.",
            "status_n8n": resposta_n8n.status_code,
            "resposta_n8n": resposta_n8n.text
        }, status_code=200)

    except Exception as e:
        logging.error("❌ Erro durante o processamento:")
        logging.error(str(e))
        return JSONResponse(content={
            "erro": "Erro ao processar ou encaminhar dados.",
            "detalhes": str(e)
        }, status_code=500)
