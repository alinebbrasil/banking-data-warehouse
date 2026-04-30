"""
generate_banking_data.py

Objetivo:
Gerar dados bancários sintéticos para alimentar um projeto de Data Warehouse.

Este script cria quatro arquivos CSV na pasta data/raw:
- customers.csv
- branches.csv
- accounts.csv
- transactions.csv

Esses arquivos simulam dados de um banco:
- clientes
- agências
- contas
- transações financeiras

Depois, vamos transformar esses dados em um modelo dimensional:
- dim_customers
- dim_branches
- dim_accounts
- dim_date
- fact_transactions
"""

from pathlib import Path
import random
import pandas as pd


# Define a semente aleatória para que os dados gerados sejam sempre os mesmos.
# Isso ajuda na reprodutibilidade do projeto.
random.seed(42)


# Caminho da pasta raiz do projeto.
# __file__ representa o caminho deste script.
# parents[1] sobe duas pastas: scripts/ -> raiz do projeto.
PROJECT_ROOT = Path(__file__).resolve().parents[1]


# Pasta onde os arquivos CSV brutos serão salvos.
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


# Cria a pasta data/raw caso ela ainda não exista.
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------
# 1. Criar tabela de clientes
# -----------------------------

customers = []

cities = [
    ("Rio de Janeiro", "RJ"),
    ("São Paulo", "SP"),
    ("Belo Horizonte", "MG"),
    ("Curitiba", "PR"),
    ("Salvador", "BA"),
    ("Recife", "PE"),
    ("Porto Alegre", "RS"),
    ("Brasília", "DF"),
]

for customer_id in range(1, 501):
    city, state = random.choice(cities)

    customers.append(
        {
            "customer_id": customer_id,
            "customer_name": f"Customer {customer_id}",
            "city": city,
            "state": state,
            "customer_segment": random.choice(["Retail", "Premium", "Corporate"]),
            "registration_date": pd.Timestamp("2020-01-01")
            + pd.Timedelta(days=random.randint(0, 1200)),
        }
    )

customers_df = pd.DataFrame(customers)


# -----------------------------
# 2. Criar tabela de agências
# -----------------------------

branches = []

for branch_id in range(1, 21):
    city, state = random.choice(cities)

    branches.append(
        {
            "branch_id": branch_id,
            "branch_name": f"Branch {branch_id}",
            "city": city,
            "state": state,
            "branch_type": random.choice(["Physical", "Digital"]),
        }
    )

branches_df = pd.DataFrame(branches)


# -----------------------------
# 3. Criar tabela de contas
# -----------------------------

accounts = []

for account_id in range(1, 801):
    accounts.append(
        {
            "account_id": account_id,
            "customer_id": random.randint(1, 500),
            "branch_id": random.randint(1, 20),
            "account_type": random.choice(["Checking", "Savings", "Salary"]),
            "opening_date": pd.Timestamp("2020-01-01")
            + pd.Timedelta(days=random.randint(0, 1400)),
            "status": random.choice(["Active", "Active", "Active", "Inactive"]),
        }
    )

accounts_df = pd.DataFrame(accounts)


# -----------------------------
# 4. Criar tabela de transações
# -----------------------------

transactions = []

transaction_types = ["Deposit", "Withdrawal", "Transfer", "Payment", "Pix"]

start_date = pd.Timestamp("2023-01-01")
end_date = pd.Timestamp("2024-12-31")
date_range_days = (end_date - start_date).days

for transaction_id in range(1, 10001):
    transaction_type = random.choice(transaction_types)

    amount = round(random.uniform(20, 8000), 2)

    # Para saídas de dinheiro, vamos usar valor negativo.
    # Isso facilita análises de entrada, saída e saldo líquido.
    if transaction_type in ["Withdrawal", "Transfer", "Payment", "Pix"]:
        amount = -amount

    transactions.append(
        {
            "transaction_id": transaction_id,
            "account_id": random.randint(1, 800),
            "transaction_date": start_date
            + pd.Timedelta(days=random.randint(0, date_range_days)),
            "transaction_type": transaction_type,
            "amount": amount,
            "channel": random.choice(["Mobile", "Internet Banking", "ATM", "Branch"]),
        }
    )

transactions_df = pd.DataFrame(transactions)


# -----------------------------
# 5. Salvar arquivos CSV
# -----------------------------

customers_df.to_csv(RAW_DATA_DIR / "customers.csv", index=False)
branches_df.to_csv(RAW_DATA_DIR / "branches.csv", index=False)
accounts_df.to_csv(RAW_DATA_DIR / "accounts.csv", index=False)
transactions_df.to_csv(RAW_DATA_DIR / "transactions.csv", index=False)


print("Arquivos gerados com sucesso em data/raw:")
print("- customers.csv")
print("- branches.csv")
print("- accounts.csv")
print("- transactions.csv")