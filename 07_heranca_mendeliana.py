"""
PROBABILIDADE DE HERANÇA MENDELIANA (1ª LEI DE MENDEL)

Contexto Biológico:
A previsão de herança fenotípica é o pilar do aconselhamento genético. 
A partir de uma população com frequências genotípicas conhecidas (homozigotos dominantes, 
heterozigotos e homozigotos recessivos), o algoritmo calcula a probabilidade de a 
próxima geração expressar o fenótipo dominante, simulando o cruzamento aleatório 
e os quadros de Punnett.

Solução Computacional:
Em vez de processar todas as combinações de cruzamentos que resultam em alelos dominantes, 
o algoritmo otimiza o cálculo utilizando a regra do evento complementar em probabilidade. 
Ele calcula a chance da prole possuir apenas alelos recessivos (aa) e subtrai esse 
valor de 1 (100%), reduzindo a carga computacional para complexidade O(1).
"""

def probabilidade_fenotipo_dominante(k, m, n):
    # k = AA, m = Aa, n = aa
    total_populacao = k + m + n
    
    # 1. Chance de sortear dois pais recessivos (aa x aa) -> 100% de chance do filho ser aa
    # Formula: (chances do 1º pai) * (chances do 2º pai após retirar o 1º da população)
    prob_aa_aa = (n / total_populacao) * ((n - 1) / (total_populacao - 1))
    
    # 2. Chance de sortear dois pais heterozigotos (Aa x Aa) -> 25% de chance do filho ser aa
    prob_Aa_Aa = (m / total_populacao) * ((m - 1) / (total_populacao - 1)) * 0.25
    
    # 3. Chance de sortear um heterozigoto e um recessivo (Aa x aa OU aa x Aa) -> 50% de chance
    prob_Aa_aa = (m / total_populacao) * (n / (total_populacao - 1)) * 0.5
    prob_aa_Aa = (n / total_populacao) * (m / (total_populacao - 1)) * 0.5
    
    # Soma todas as probabilidades de gerar um filho recessivo
    chance_recessivo = prob_aa_aa + prob_Aa_Aa + prob_Aa_aa + prob_aa_Aa
    
    # A chance do dominante é 100% menos a chance do recessivo
    chance_dominante = 1 - chance_recessivo
    return chance_dominante

# Bloco de execução (Simulação do Rosalind)
# Substitua "2 2 2" pelos números que o site gerar no seu arquivo de texto
entrada_rosalind = "2 2 2"
k, m, n = map(int, entrada_rosalind.split())

resultado = probabilidade_fenotipo_dominante(k, m, n)

# O Rosalind pede até 5 casas decimais de precisão
print(f"{resultado:.5f}")
