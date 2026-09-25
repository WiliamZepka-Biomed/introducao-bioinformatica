"""
FERRAMENTA DE ANÁLISE DE COMPOSIÇÃO DE BASES

Contexto Biológico:
A quantificação de nucleotídeos é um parâmetro crítico na rotina de biologia molecular. 
O cálculo da proporção entre bases púricas e pirimídicas e a determinação do teor de 
Guanina e Citosina (conteúdo GC) são essenciais para prever a estabilidade térmica da 
dupla hélice de DNA e para o desenho acurado de primers de PCR.

Solução Computacional:
O algoritmo analisa sequências genômicas por meio do método nativo .count() do Python. 
Ele realiza uma varredura otimizada em tempo linear O(n) na cadeia de caracteres, 
extraindo a frequência absoluta de cada base sem a necessidade de bibliotecas pesadas.
"""

def analisar_composicao_dna(sequencia_dna):
    """
    Recebe uma fita de DNA e retorna a contagem absoluta de A, C, G e T.
    """
    a = sequencia_dna.count('A')
    c = sequencia_dna.count('C')
    g = sequencia_dna.count('G')
    t = sequencia_dna.count('T')
    
    return f"Adenina: {a} | Citosina: {c} | Guanina: {g} | Timina: {t}"

# Simulação com dados brutos do sequenciador
fita_bruta = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
resultado = analisar_composicao_dna(fita_bruta)
print(resultado)
