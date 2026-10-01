
import os
import urllib.request

from extrair_dados import ARQUIVO_ENTRADA, extrair_palestrantes

BASE_URL = "https://eventos.ifgoiano.edu.br"
PASTA_DOWNLOAD = "download"


def baixar_imagens(palestrantes: list[dict], pasta_destino: str = PASTA_DOWNLOAD) -> list[dict]:
    os.makedirs(pasta_destino, exist_ok=True)

    for palestrante in palestrantes:
        url_imagem = BASE_URL + palestrante["imagem_url"]
        nome_arquivo = os.path.basename(palestrante["imagem_url"])
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)

        requisicao = urllib.request.Request(url_imagem, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(requisicao, timeout=30) as resposta:
            conteudo = resposta.read()

        with open(caminho_destino, "wb") as arquivo_imagem:
            arquivo_imagem.write(conteudo)

        palestrante["imagem_arquivo"] = nome_arquivo

    return palestrantes


if __name__ == "__main__":
    with open(ARQUIVO_ENTRADA, encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palestrantes = extrair_palestrantes(texto)
    palestrantes = baixar_imagens(palestrantes)

    for p in palestrantes:
        print(f"Imagem salva: {p['imagem_arquivo']} ({p['nome']})")
