import os
import requests
import logging

# Função para enviar mensagem via Z-API
# Recebe o número do contato e a mensagem personalizada
# Todos os erros são tratados e logados de forma amigável
def enviar_mensagem(numero, mensagem):
    # Recupera as credenciais da Z-API do ambiente
    ZAPI_TOKEN = os.getenv('ZAPI_TOKEN')
    ZAPI_INSTANCE = os.getenv('ZAPI_INSTANCE')
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE}/token/{ZAPI_TOKEN}/send-message"
    payload = {
        "phone": numero,
        "message": mensagem
    }
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            logging.info(f"Mensagem enviada com sucesso para o número {numero}!")
        else:
            logging.error(f"Falha ao enviar mensagem para {numero}. Resposta da API: {r.text}")
            logging.error("Verifique se o número está correto, se a instância está ativa e se o token é válido.")
    except Exception as e:
        logging.error(f"Erro inesperado ao tentar enviar mensagem para {numero}: {e}")
        logging.error("Verifique sua conexão com a internet e as credenciais da Z-API.")
