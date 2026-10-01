
from extrair_dados import ARQUIVO_ENTRADA, extrair_palestrantes
from download_imagens import PASTA_DOWNLOAD, baixar_imagens
from criar_banco import ARQUIVO_BANCO, criar_banco
import sqlite3

SQL_INSERIR = "INSERT INTO speaker (name, work, email, image) VALUES (?, ?, ?, ?)"


def popular_banco(palestrantes: list[dict], caminho_banco: str = ARQUIVO_BANCO) -> None:
    conexao = sqlite3.connect(caminho_banco)
    try:
        conexao.execute("DELETE FROM speaker")
        for palestrante in palestrantes:
            conexao.execute(
                SQL_INSERIR,
                (
                    palestrante["nome"],
                    palestrante["trabalho"],
                    palestrante["contato"],
                    palestrante["imagem_arquivo"],
                ),
            )
        conexao.commit()
    finally:
        conexao.close()


if __name__ == "__main__":
    with open(ARQUIVO_ENTRADA, encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palestrantes = extrair_palestrantes(texto)
    palestrantes = baixar_imagens(palestrantes, PASTA_DOWNLOAD)

    criar_banco()
    popular_banco(palestrantes)

    print(f"{len(palestrantes)} palestrantes registrados em {ARQUIVO_BANCO}.")
