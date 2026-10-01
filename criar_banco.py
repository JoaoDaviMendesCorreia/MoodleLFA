
import sqlite3

ARQUIVO_BANCO = "event.db"

SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS speaker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    work VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL
);
"""


def criar_banco(caminho_banco: str = ARQUIVO_BANCO) -> None:
    conexao = sqlite3.connect(caminho_banco)
    try:
        conexao.execute(SQL_CRIAR_TABELA)
        conexao.commit()
    finally:
        conexao.close()


if __name__ == "__main__":
    criar_banco()
    print(f"Banco de dados criado em: {ARQUIVO_BANCO}")
