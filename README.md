Para contar ocorrências de uma letra em várias palavras em Python, você pode usar um simples loop para percorrer as palavras e a função count para contar quantas vezes a letra aparece em cada palavra. Aqui está um exemplo de como fazer isso:

python
Copiar código
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
Neste código, a função contar_ocorrencias recebe uma letra e uma lista de palavras, e retorna o total de ocorrências da letra nas palavras. Você pode modificar a lista de palavras e a letra conforme necessário.
