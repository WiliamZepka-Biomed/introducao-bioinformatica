"""
GERADOR DE COMPLEMENTO REVERSO (REVERSE COMPLEMENT)

Contexto Biológico:
A dupla hélice do DNA é formada por duas fitas antiparalelas ligadas por pontes de 
hidrogênio entre pares de bases complementares (Adenina-Timina e Citosina-Guanina). 
A extração do complemento reverso simula computacionalmente a fita oposta na direção 
biológica correta (5' para 3'). Este processo é o alicerce para o desenho de 
primers de PCR, sondas moleculares e alinhamento de sequências (NGS).

Solução Computacional:
O algoritmo evita loops lentos (for/while) utilizando funções nativas de mapeamento 
em C do Python (maketrans e translate) para criar um dicionário de substituição 
simultânea das bases. O fatiamento reverso (slicing [::-1]) inverte a ordem da fita, 
garantindo eficiência com complexidade de tempo O(n).
"""

def gerar_complemento_reverso(sequencia_dna):
    # 1. Cria a regra química de emparelhamento: A->T, T->A, C->G, G->C
    regra_emparelhamento = str.maketrans('ATCG', 'TAGC')
    
    # 2. translate() troca as letras e o [::-1] inverte o texto de trás para frente
    fita_complementar_reversa = sequencia_dna.translate(regra_emparelhamento)[::-1]
    
    return fita_complementar_reversa

# Bloco de execução (Simulação do Rosalind)
fita_bruta = "AAAACCCGGT"
resultado = gerar_complemento_reverso(fita_bruta)

print(f"Fita Original:           {fita_bruta}")
print(f"Complemento Reverso:     {resultado}")
