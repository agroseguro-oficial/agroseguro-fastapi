# AgroSeguro FastAPI

Este é o backend FastAPI do projeto AgroSeguro. Ele recebe dados estruturados do Assistente GPT e encaminha para o n8n.

## Rota principal

POST `/receber-analise`

Recebe um JSON da análise e envia para o webhook ativo no n8n.

## Deploy

Compatível com plataformas como Render, Heroku e Replit.