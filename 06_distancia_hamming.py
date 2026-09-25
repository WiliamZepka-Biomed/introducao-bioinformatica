"""
DETECÇÃO DE MUTAÇÕES PONTUAIS (DISTÂNCIA DE HAMMING)

Contexto Biológico:
A Distância de Hamming quantifica o número de substituições de bases (mutações pontuais 
ou SNPs - Single Nucleotide Polymorphisms) entre sequências homólogas. Na prática clínica 
e epidemiológica, este cálculo determina a taxa de divergência evolutiva entre cepas virais 
ou identifica variantes genéticas de um paciente em relação ao genoma humano de referência. 
É o princípio algorítmico fundamental da etapa de 'Variant Calling' em pipelines de NGS.

Solução Computacional:
O algoritmo opera com complexidade de tempo linear O(n). Utiliza a função nativa 'zip()' 
do Python para emparelhar as duas strings índice por índice (como os dentes de um zíper), 
permitindo a comparação simultânea das bases sem a necessidade de controle manual de índices.
"""

def calcular_distancia_hamming(fita_1, fita_2):
    mutacoes = 0
    
    # zip() junta as duas fitas lado a lado. Ex: ('G', 'C'), ('A', 'A')...
    for base1, base2 in zip(fita_1, fita_2):
        if base1 != base2:
            mutacoes += 1
            
    return mutacoes

# Bloco de execução (Simulação do Rosalind)
entrada_rosalind = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""

# Divide o texto do Rosalind nas duas fitas usando a quebra de linha (\n)
fita_s, fita_t = entrada_rosalind.strip().split('\n')

resultado = calcular_distancia_hamming(fita_s, fita_t)
print(resultado)
