import logging
from dotenv import load_dotenv
from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem
import os

# Carrega variáveis do .env explicitamente da raiz do projeto
# Isso garante que as credenciais sejam lidas corretamente, independente de onde o script é executado
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

# Exibe as variáveis carregadas para facilitar o debug inicial
print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))
print("SUPABASE_KEY:", os.getenv("SUPABASE_KEY"))

# Configuração de logs simples e legíveis
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mensagem personalizada que será enviada para cada contato
MENSAGEM = "Olá, {{nome_completo}}! Esta é uma mensagem automática."

# Função principal do sistema
# Busca os contatos no Supabase e envia mensagem personalizada via Z-API
# Todos os erros são tratados e logados de forma amigável

def main():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    try:
        contatos = buscar_contatos(supabase_url, supabase_key)
        if not contatos:
            logging.warning("Nenhum contato encontrado no banco. Verifique se há dados cadastrados.")
        for contato in contatos:
            nome = contato.get('nome_completo', 'Contato')
            numero = contato.get('numero')
            if not numero:
                logging.warning(f"Contato '{nome}' não possui número cadastrado. Pulando...")
                continue
            mensagem = MENSAGEM.replace("{{nome_completo}}", nome)
            logging.info(f"Enviando mensagem para {nome} ({numero})...")
            enviar_mensagem(numero, mensagem)
    except Exception as e:
        logging.error(f"Erro inesperado na execução principal: {e}")
        logging.error("Verifique suas credenciais, conexão com Supabase e Z-API, e tente novamente.")

if __name__ == "__main__":
    main()
