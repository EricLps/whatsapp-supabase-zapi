import os
import logging
from dotenv import load_dotenv
from services.contatos_service import buscar_contatos
from services.mensagem_service import enviar_mensagem

#exibe data/hora e mensagem de forma simples
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# carrega as credenciais do arquivo .env
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

#mensagem que será personalizada com o nome de cada contato
MENSAGEM = "Olá, {{nome}}! Esta é uma mensagem automática do sistema."

def main():
    """
    Função principal:
    1. Busca todos os contatos cadastrados no supabase
    2. Pra cada contato, personaliza a mensagem com o nome
    3. Envia a mensagem pelo WhatsApp usando Z-api
    """
    logging.info("🚀 Iniciando sistema de envio de mensagens...")

    # Busca todos os contatos na tabela do Supabase
    contatos = buscar_contatos()

    if not contatos:
        logging.warning("⚠️ Nenhum contato encontrado na base de dados!")
        return

    logging.info(f"📱 Preparando envio para {len(contatos)} contato(s)")

    # Processa os contatos individualmente
    for contato in contatos:
        nome = contato.get('nome_completo', 'Amigo')
        numero = contato.get('numero')

        # Pula contatos sem número cadastrado
        if not numero:
            logging.warning(f"⚠️ Contato '{nome}' não possui número - pulando...")
            continue

        # Personaliza a mensagem substituindo {{nome}}
        mensagem_personalizada = MENSAGEM.replace("{{nome}}", nome)

        # registra o envio e chama a função para enviar
        logging.info(f"📤 Enviando para {nome} ({numero})")
        enviar_mensagem(numero, mensagem_personalizada)

    logging.info("✅ Processo concluído!")

if __name__ == "__main__":
    main()
