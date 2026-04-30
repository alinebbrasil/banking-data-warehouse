"""
run_sql_file.py

Objetivo:
Executar arquivos SQL no banco SQLite do projeto.

Uso:
python scripts/run_sql_file.py sql/01_create_dw_tables.sql
"""

from pathlib import Path
import sys
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "banking.db"


def run_sql_file(sql_file_path: Path) -> None:
    """
    Executa um arquivo SQL inteiro no banco SQLite.

    Args:
        sql_file_path: caminho do arquivo .sql que será executado.
    """
    if not sql_file_path.exists():
        raise FileNotFoundError(f"Arquivo SQL não encontrado: {sql_file_path}")

    sql_script = sql_file_path.read_text(encoding="utf-8")

    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.executescript(sql_script)
        connection.commit()

    print(f"Arquivo SQL executado com sucesso: {sql_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso correto:")
        print("python scripts/run_sql_file.py sql/01_create_dw_tables.sql")
        sys.exit(1)

    sql_file = PROJECT_ROOT / sys.argv[1]
    run_sql_file(sql_file)