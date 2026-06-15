def limpar_texto(texto):
    texto = texto.lower()
    carcteres = ",.%*!|?;:\"'()[]{}"
    for char in carcteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras (frase):
    frase = limpar_texto(frase)
    palavras = frase.split()
    print(palavras)
    return len(palavras)
