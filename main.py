
from download_pagina import baixar_pagina
from extrair_dados import extrair_palestrantes
from download_imagens import baixar_imagens
from criar_banco import criar_banco
from popular_banco import popular_banco


def main() -> None:
    caminho_pagina = baixar_pagina()
    print(f"[002] Pagina salva em: {caminho_pagina}")

    with open(caminho_pagina, encoding="utf-8") as arquivo:
        texto = arquivo.read()

    palestrantes = extrair_palestrantes(texto)
    print(f"[003] {len(palestrantes)} palestrantes extraidos")

    palestrantes = baixar_imagens(palestrantes)
    print("[004] Imagens salvas na pasta 'download'")

    criar_banco()
    print("[005] Banco de dados 'event.db' criado/verificado")

    popular_banco(palestrantes)
    print(f"[006] {len(palestrantes)} palestrantes registrados na tabela 'speaker'")


if __name__ == "__main__":
    main()
