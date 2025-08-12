import os
import logging
import requests

def enviar_mensagem(numero, mensagem):
    """
    envia a mensagem personalizada pelo WhatsApp
    Args:
        numero (str): Número do WhatsApp (formato: 5511999999999)
        mensagem (str): Texto da mensagem a ser enviada
    Returns:
        None: Apenas registra logs do resultado da operação
    """
    try:
        token = os.getenv('ZAPI_TOKEN')
        instance = os.getenv('ZAPI_INSTANCE')

        # Monta a URL da API com instância e token
        url = f"https://api.z-api.io/instances/{instance}/token/{token}/send-message"

        #dados da mensagem no formato esperado pela Z-API
        dados = {"phone": numero, "message": mensagem}

        #requisição POST para a z-api
        resposta = requests.post(url, json=dados)

        #verifica se o envio foi um sucesso
        if resposta.status_code == 200:
            logging.info(f"✅ Mensagem enviada com sucesso para {numero}")
        else:
            logging.error(f"❌ Falha no envio para {numero}: {resposta.text}")
            logging.error("💡 Verifique: token, instância ativa e formato do número")

    except Exception as e:
        logging.error(f"❌ Erro inesperado ao enviar para {numero}: {e}")
        logging.error("💡 Verifique: conexão com internet e credenciais da Z-API")
