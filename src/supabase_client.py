import os
from supabase import create_client, Client
import logging

# Função para buscar contatos no Supabase
# Busca até 3 contatos na tabela Zapbase e retorna uma lista de dicionários
# Todos os erros são tratados e logados de forma amigável
def buscar_contatos(supabase_url, supabase_key):
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        response = supabase.table('Zapbase').select('nome_completo,numero').limit(3).execute()
        contatos = response.data
        logging.info(f"{len(contatos)} contatos encontrados no Supabase.")
        return contatos
    except Exception as e:
        logging.error(f"Erro ao buscar contatos no Supabase: {e}")
        logging.error("Verifique se a tabela Zapbase existe, se as colunas estão corretas e se as credenciais estão válidas.")
        return []
