
import urllib.request

URL = "https://eventos.ifgoiano.edu.br/integra2026/"
ARQUIVO_SAIDA = "pagina_integra2026.txt"


def baixar_pagina(url: str = URL, caminho_saida: str = ARQUIVO_SAIDA) -> str:
    requisicao = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(requisicao, timeout=30) as resposta:
        codigo_fonte = resposta.read().decode("utf-8")

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        arquivo.write(codigo_fonte)

    return caminho_saida


if __name__ == "__main__":
    caminho = baixar_pagina()
    print(f"Codigo-fonte salvo em: {caminho}")
