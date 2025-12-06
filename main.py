import heapq
import re

# Classe Nó da Árvore de Huffman
class Node:
    def __init__(self, freq=0, palavra=None, esq=None, dir=None):
        self.palavra = palavra
        self.freq = freq
        self.esq = esq 
        self.dir = dir

    def __lt__(self, other):
        return self.freq < other.freq


# Função para contar a frequência das palavras
def contar_frequencia(texto):
    palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", texto.lower()) # Converte para minúsculas, optei por não normalizar acentos para evitar ambiguidades
    freq = {}                                             
    for p in palavras:
        freq[p] = freq.get(p, 0) + 1
    return freq


# Função para criar a àrvore
def criar_arvore(freq_map):
    heap = []

    # Cria um nó para cada palavra
    for palavra, freq in freq_map.items():
        heapq.heappush(heap, Node(palavra=palavra, freq=freq))

    # Constrói a árvore
    while len(heap) > 1:
        primeiro = heapq.heappop(heap)
        segundo = heapq.heappop(heap)

        novo = Node(
            freq=primeiro.freq + segundo.freq,
            esq=primeiro,
            dir=segundo
        )

        heapq.heappush(heap, novo)

    return heap[0] if heap else None


# Gera código de Huffman para cada palavra
def gerar_codigos(node, prefixo="", tabela=None):
    if tabela is None:
        tabela = {}

    # Nó folha
    if node.palavra is not None:
        # Retorna "0" se for uma única palavra
        tabela[node.palavra] = prefixo if prefixo != "" else "0"
        return tabela

    # Percorre a esquerda
    if node.esq:
        gerar_codigos(node.esq, prefixo + "0", tabela)

    # Percorre a direita
    if node.dir:
        gerar_codigos(node.dir, prefixo + "1", tabela)

    return tabela

# Comprime o texto 
def comprimir(texto, codigos):
    palavras = re.findall(r"[a-zA-ZÀ-ÿ]+", texto.lower())
    bits = "".join(codigos[p] for p in palavras)
    return bits


# Imprime árvore em forma de texto
def serializar_arvore(node, lista=None):
    if lista is None:
        lista = []

    if node.palavra is not None:
        lista.append(f"L({node.palavra})")
    else:
        lista.append("N")
        serializar_arvore(node.esq, lista)
        serializar_arvore(node.dir, lista)

    return " ".join(lista)

def imprimir_arvore_LR(node, prefixo="", lado="Raiz", linhas=None):
    if linhas is None:
        linhas = []

    if node is None:
        return linhas

    # Mostra a palavra se for uma folha
    if node.palavra is not None:
        linhas.append(f"{prefixo}{lado} -> {node.palavra} ({node.freq})")
    else:
        linhas.append(f"{prefixo}{lado} -> * ({node.freq})")

    novo_prefixo = prefixo + "    "

    # Esquerda (0) depois direita (1)
    if node.esq:
        imprimir_arvore_LR(node.esq, novo_prefixo, "L", linhas)
    if node.dir:
        imprimir_arvore_LR(node.dir, novo_prefixo, "R", linhas)

    return linhas


def processar():
    with open("data/input.dat", "r", encoding="utf-8") as f:
        conteudo = f.read().strip()

    textos = [t.strip() for t in conteudo.split("\n\n")]
    saida = []

    for i, texto in enumerate(textos, start=1):
        freq = contar_frequencia(texto)
        arvore = criar_arvore(freq)
        codigos = gerar_codigos(arvore)
        comprimido = comprimir(texto, codigos)
        arvore_serializada = serializar_arvore(arvore)
        arvore_visual = imprimir_arvore_LR(arvore)

        bloco = []
        bloco.append(f"=== TEXTO {i} ===")
        bloco.append("\nFrase inicial: ")
        bloco.append(texto)
        bloco.append("\nÁrvore textual: ")
        bloco.append(arvore_serializada)
        bloco.append("\nÁrvore visual: ")
        bloco.extend(arvore_visual)

        bloco.append("\nCódigos de Huffman:")
        for palavra, codigo in codigos.items():
            bloco.append(f"{palavra} : {codigo}")

        bloco.append("\nTexto Comprimido: ")
        bloco.append(comprimido)

        saida.append("\n".join(bloco))

    with open("data/output.dat", "w", encoding="utf-8") as f:
        f.write("\n\n".join(saida))

    print("Arquivo output.dat gerado.")

if __name__ == "__main__":
    processar()
