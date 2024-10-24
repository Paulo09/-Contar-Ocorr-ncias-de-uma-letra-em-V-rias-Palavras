# Contar Ocorrências de uma letra em Várias Palavras



def contar_ocorrencias(letra, palavras):
    total_ocorrencias = 0
    for palavra in palavras:
        total_ocorrencias += palavra.count(letra)
    return total_ocorrencias

# Exemplo de uso
palavras = ["banana", "maçã", "laranja", "abacaxi"]
letra = "a"
ocorrencias = contar_ocorrencias(letra, palavras)

print(f"A letra '{letra}' aparece {ocorrencias} vezes nas palavras.")
