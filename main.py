from fastapi import FastAPI, Request
import requests

app = FastAPI()

N8N_WEBHOOK_URL = "https://agroseguro.app.n8n.cloud/webhook/salvar-dados-nf"

@app.post("/receber-analise")
async def receber_analise(solicitar: Request):
    try:
        dados = await solicitar.json()
        print("🧾 Dados recebidos do Assistente:")
        print(dados)

        resposta_n8n = requests.post(N8N_WEBHOOK_URL, json=dados)
        print("📤 Enviado ao n8n:")
        print(resposta_n8n.status_code)
        print(resposta_n8n.text)

        return {
            "mensagem": "Dados recebidos e encaminhados ao n8n com sucesso.",
            "status_n8n": resposta_n8n.status_code,
            "resposta_n8n": resposta_n8n.text
        }

    except Exception as erro:
        print("❌ Erro ao processar requisição:", erro)
        return {
            "mensagem": "Erro ao processar requisição",
            "erro": str(erro)
        }
