palavras = ("python", "programação", "computador", "código", "desenvolvimento",
            "tecnologia", "software", "algoritmo", "dados", "rede",
            "internet", "função", "variável", "estrutura", "sintaxe")
contletra
for cont in palavras:
    for letra in cont:
        if letra.lower() in 'aeiou':
            contletra+=1
    print(f'na palavra {palavras[cont]}')