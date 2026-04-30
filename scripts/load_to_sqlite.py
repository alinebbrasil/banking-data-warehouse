"""
load_to_sqlite.py

Objetivo:
Carregar os arquivos CSV gerados anteriormente em um banco SQLite.

Vamos:
1. Ler os CSVs
2. Criar um banco SQLite
3. Criar tabelas no banco
4. Inserir os dados

Resultado:
Um arquivo banking.db com as tabelas:
- customers
- branches
- accounts
- transactions
"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine


# Caminho da raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Caminho dos dados brutos
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

# Caminho do banco SQLite (vai ser criado automaticamente)
DB_PATH = PROJECT_ROOT / "banking.db"


# -----------------------------
# 1. Criar conexão com SQLite
# -----------------------------

# sqlite:/// significa:
# "criar ou conectar a um banco SQLite nesse caminho"
engine = create_engine(f"sqlite:///{DB_PATH}")

print("Conexão com SQLite criada.")


# -----------------------------
# 2. Ler os arquivos CSV
# -----------------------------

customers_df = pd.read_csv(RAW_DATA_DIR / "customers.csv")
branches_df = pd.read_csv(RAW_DATA_DIR / "branches.csv")
accounts_df = pd.read_csv(RAW_DATA_DIR / "accounts.csv")
transactions_df = pd.read_csv(RAW_DATA_DIR / "transactions.csv")

print("CSV carregados com sucesso.")


# -----------------------------
# 3. Salvar no banco
# -----------------------------

# if_exists="replace" → substitui a tabela se já existir
customers_df.to_sql("customers", engine, if_exists="replace", index=False)
branches_df.to_sql("branches", engine, if_exists="replace", index=False)
accounts_df.to_sql("accounts", engine, if_exists="replace", index=False)
transactions_df.to_sql("transactions", engine, if_exists="replace", index=False)

print("Dados carregados no SQLite com sucesso.")


# -----------------------------
# 4. Teste simples
# -----------------------------

query = "SELECT COUNT(*) as total FROM transactions"

result = pd.read_sql(query, engine)

print("Total de transações no banco:")
print(result)