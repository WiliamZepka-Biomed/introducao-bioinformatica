"""
A transcrição é a primeira etapa da expressão génica, onde a sequência de DNA é copiada para gerar o RNA mensageiro (mRNA).
Na bioinformática, esta etapa é o pré-requisito para algoritmos de tradução, permitindo prever a cadeia de aminoácidos (proteína)
que será sintetizada pelo ribossoma. A substituição química essencial neste processo é a troca da Timina (T) pelo Uracilo (U).

Solução Computacional:
A manipulação direta de texto em Python substitui a necessidade de carregar bibliotecas complexas para tarefas simples.
O método .replace() localiza e substitui os caracteres em toda a extensão do genoma de forma instantânea, simulando computacionalmente a ação da enzima RNA polimerase.
"""

# Script: 02_transcricao_in_silico.py

def transcrever_dna_para_rna(sequencia_dna):
    """
    Simula a transcrição biológica substituindo Timina (T) por Uracilo (U).
    """
    rna_mensageiro = sequencia_dna.replace('T', 'U')
    return rna_mensageiro

# Simulação de transcrição de um gene alvo
gene_dna = "GATGGAACTTGACTACGTAAATT"
mrna_gerado = transcrever_dna_para_rna(gene_dna)

print(f"Fita Original (DNA): {gene_dna}")
print(f"Fita Transcrita (RNA): {mrna_gerado}")
