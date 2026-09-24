# Script: 01_composicao_bases.py

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
