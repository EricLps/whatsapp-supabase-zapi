import os
import logging
from dotenv import load_dotenv
from supabase import create_client, Client

def buscar_contatos():
    """
    conecta com o Supabase e busca todos os contatos da tabela 'Zapbase'
    retorna:
        list: Lista de dicionários com 'nome_completo' e 'numero' dos contatos
        list: Lista vazia em caso de erro
    """
    try:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")

        #conecta com o banco Supabase
        supabase = create_client(supabase_url, supabase_key)

        # Busca TODOS os contatos com nome e número
        response = supabase.table('Zapbase').select('nome_completo,numero').execute()

        contatos = response.data
        logging.info(f"📊 Encontrados {len(contatos)} contatos na base de dados")
        return contatos

    except Exception as e:
        logging.error(f"❌ Erro ao conectar com Supabase: {e}")
        logging.error("💡 Verifique: URL, chave de API, nome da tabela e conexão com internet")
        return []
