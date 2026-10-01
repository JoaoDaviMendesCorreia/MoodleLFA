
import json
import re

ARQUIVO_ENTRADA = "pagina_integra2026.txt"

REGEX_CARD = re.compile(
    r'id="Palestrante\d+">.*?'
    r'<img src="(?P<imagem>/media/static/palestrantes/[^"]+)"[^>]*>\s*'
    r'<p class="card-text"[^>]*>(?P<nome>[^<]+)</p>',
    re.DOTALL,
)

REGEX_MODAL = re.compile(
    r'<div class="modal fade" id="modal\d+">.*?'
    r'<h4>(?P<nome_modal>[^<]+)</h4>\s*<br>\s*<h6>(?P<trabalho>[^<]+)</h6>'
    r'.*?<div class="modal-body">(?P<corpo>.*?)</div>\s*<div class="modal-footer">',
    re.DOTALL,
)

REGEX_EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')


def extrair_palestrantes(texto: str) -> list[dict]:
    cartoes = [
        {"imagem": m.group("imagem").strip(), "nome": m.group("nome").strip()}
        for m in REGEX_CARD.finditer(texto)
    ]

    modais = []
    for m in REGEX_MODAL.finditer(texto):
        email_encontrado = REGEX_EMAIL.search(m.group("corpo"))
        modais.append(
            {
                "trabalho": m.group("trabalho").strip(),
                "contato": email_encontrado.group(0) if email_encontrado else "",
            }
        )

    palestrantes = []
    for cartao, modal in zip(cartoes, modais):
        palestrantes.append(
            {
                "nome": cartao["nome"],
                "imagem_url": cartao["imagem"],
                "trabalho": modal["trabalho"],
                "contato": modal["contato"],
            }
        )
    return palestrantes


if __name__ == "__main__":
    with open(ARQUIVO_ENTRADA, encoding="utf-8") as arquivo:
        texto = arquivo.read()

    dados = extrair_palestrantes(texto)

    with open("dados_palestrantes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)

    print(f"{len(dados)} palestrantes extraidos.")
    for p in dados:
        print(f"- {p['nome']} | {p['trabalho']} | {p['contato']} | {p['imagem_url']}")
