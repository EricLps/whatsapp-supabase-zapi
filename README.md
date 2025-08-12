# Zapbase: Envio automatizado de mensagens WhatsApp via Supabase e Z-API

Aplicação Python que integra Supabase e Z-API para enviar mensagens personalizadas via WhatsApp de forma automatizada, buscando contatos no banco e tratando erros com logs claros.

## Configuração da tabela no Supabase
1. Crie um projeto no Supabase
2. Crie uma tabela chamada `Zapbase` com os campos:
   - `id` (integer, primary key)
   - `nome_completo` (text)
   - `numero` (text)
3. Configure Row Level Security (RLS) e crie uma política de leitura pública

## Variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_api_do_supabase
ZAPI_TOKEN=seu_token_da_zapi
ZAPI_INSTANCE=seu_id_da_instancia_zapi
```

## Instalação e execução
```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o projeto
cd src
python main.py
```

## Funcionalidades
✅ Busca todos os contatos cadastrados no Supabase  
✅ Personaliza mensagens com o nome de cada contato  
✅ Envia mensagens via WhatsApp usando Z-API  
✅ Logs informativos com emojis para acompanhar o processo  
✅ Tratamento de erros com dicas de solução  

## Estrutura do projeto
```
Zapbase/
├── .env                           # Credenciais (não versionar)
├── requirements.txt               # Dependências
└── src/
    ├── main.py                   # Arquivo principal
    └── services/
        ├── contatos_service.py   # Integração Supabase
        └── mensagem_service.py   # Integração Z-API
```
