
# AgroSeguro FastAPI

Este é o backend mínimo em FastAPI para receber dados do assistente e enviá-los ao n8n via webhook.

## Como usar no Render

1. Crie um novo projeto em https://render.com
2. Escolha "New Web Service"
3. Conecte seu GitHub e selecione este repositório
4. Certifique-se de definir:
   - Python 3.9 ou superior
   - Start command: uvicorn main:app --host 0.0.0.0 --port 10000
5. Após o deploy, acesse a URL gerada e adicione `/receber-analise`

Essa será sua nova API pública para o Assistente AgroSeguro.
