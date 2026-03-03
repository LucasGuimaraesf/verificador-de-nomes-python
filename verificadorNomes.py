import unicodedata


def normalizar_texto(texto: str) -> str:
    """
    Remove acentos, converte para minúsculo e remove espaços extras.
    """
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto.strip().lower()


def comparar_listas(lista_pdf: list, lista_excel: list) -> dict:
    """
    Compara os nomes da lista_pdf com lista_excel.
    Retorna os encontrados e não encontrados.
    """
    # Normaliza a lista do Excel
    lista_excel_normalizada = {
        normalizar_texto(nome): nome
        for nome in lista_excel
    }

    encontrados = []
    nao_encontrados = []

    for nome_pdf in lista_pdf:
        nome_normalizado = normalizar_texto(nome_pdf)

        if nome_normalizado in lista_excel_normalizada:
            encontrados.append(nome_pdf)
        else:
            nao_encontrados.append(nome_pdf)

    return {
        "encontrados": encontrados,
        "nao_encontrados": nao_encontrados
    }

listaPDF = ["nome1","nome2","nome3",...]

listaExcel = ["nome1","nome2","nome3",...]


resultado = comparar_listas(listaExcel, listaPDF)

print("Encontrados:")
for nome in resultado["encontrados"]:
    print("-", nome)

print("\nNão encontrados:")
for nome in resultado["nao_encontrados"]:
    print("-", nome)
