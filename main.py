@app.post("/receber-analise")
async def receber_analise(request: Request):
    try:
        dados = await request.json()
        print("📥 Dados recebidos do GPT:")
        print(dados)

        async with httpx.AsyncClient() as client:
            response = await client.post(N8N_WEBHOOK_URL, json=dados)

        print("📤 Resposta do n8n:")
        print(f"Status: {response.status_code}")
        print(f"Corpo: {response.text}")

        return JSONResponse(content={
            "mensagem": "Dados recebidos e encaminhados ao n8n com sucesso.",
            "status_n8n": response.status_code,
            "resposta_n8n": response.text
        })

    except Exception as e:
        print("❌ Erro durante envio ao n8n:", str(e))
        return JSONResponse(status_code=500, content={"erro": str(e)})
