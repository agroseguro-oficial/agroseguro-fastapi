from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

N8N_WEBHOOK_URL = "https://agroseguro.app.n8n.cloud/webhook/salvar-dados-nf"

@app.post("/receber-analise")
async def receber_analise(request: Request):
    try:
        dados = await request.json()

        async with httpx.AsyncClient() as client:
            response = await client.post(N8N_WEBHOOK_URL, json=dados)

        return JSONResponse(content={
            "mensagem": "Dados recebidos e encaminhados ao n8n com sucesso.",
            "status_n8n": response.status_code,
            "resposta_n8n": response.text
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
