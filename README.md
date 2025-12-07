# Codificação de Texto com Árvore de Huffman
Esse projeto implemente a compressão de texto sem perdas utilizando o **Algortimo de Huffman**, gerando códigos binários com base na frequência de palavras em um texto de entrada.

## 1. Funcionalidades
* Contagem automática de frequência das palavras
* Construção da árvore de Huffman com `heapq`
* Geração de códigos binários
* Compressão do texto
* Visualização da árvore em **dois formatos**
* Entrada e saída via arquivos

## 2. Estrutura do Projeto
```
codigo-huffman/
├── main.py 
├── README.md
└── data/
    ├── input.dat
    └── output.dat 
```
O arquivo `input.dat` deve conter um ou mais textos, separados por uma linha em branco.

Exemplo:
```
O computador executa instruções em alta velocidade e processa dados com precisão.

A memória armazena informações que são acessadas rapidamente pela CPU.

Os sistemas operacionais controlam os recursos e coordenam as tarefas do processador.
```

## 3. Como executar
Certifique-se de ter Python 3 instalado. No terminal, execute:
```
python main.py
```
Ao finalizar, o programa irá gerar um `data/output.dat` contendo:
* Texto original
* Árvore em formato textual
* Árvore visual (para facilitar a correção)
* Tabela com código de cada palavra
* Texto comprimido

## 4. Exemplo de saída
```
=== TEXTO 1 ===

Frase inicial: 
O computador executa instruções em alta velocidade e processa dados com precisão.

Árvore textual: 
N N N L(dados) L(processa) N L(com) L(alta) N N N L(e) L(instruções) N L(computador) L(em) N N L(o) L(executa) N L(velocidade) L(precisão)

Árvore visual: 
Raiz -> * (12)
    L -> * (4)
        L -> * (2)
            L -> dados (1)
            R -> processa (1)
        R -> * (2)
            L -> com (1)
            R -> alta (1)
    R -> * (8)
        L -> * (4)
            L -> * (2)
                L -> e (1)
                R -> instruções (1)
            R -> * (2)
                L -> computador (1)
                R -> em (1)
        R -> * (4)
            L -> * (2)
                L -> o (1)
                R -> executa (1)
            R -> * (2)
                L -> velocidade (1)
                R -> precisão (1)

Códigos de Huffman:
dados : 000
processa : 001
com : 010
alta : 011
e : 1000
instruções : 1001
computador : 1010
em : 1011
o : 1100
executa : 1101
velocidade : 1110
precisão : 1111

Texto Comprimido: 
11001010110110011011011111010000010000101111
```
# 5. Observações
* Palavras com acentos são *preservadas* e consideradas distintas para evitar ambiguidades.(Exemplo: Polícia ≠ Policia)
* Todo texto é convertido para letras minúsculas
* Quando há apenas uma palavra, ela recebe o código `"0"`

# Autor
Ádrian Henrique de Abreu Paiva















