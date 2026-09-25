"""
ANALISADOR DE CONTEÚDO GC E PARSER DE FASTA

Contexto Biológico:
O "Conteúdo GC" (porcentagem de Citosinas e Guaninas) dita a estabilidade termodinâmica da 
molécula de DNA, pois o pareamento G-C possui três pontes de hidrogênio (contra duas de A-T). 
Regiões ricas em GC são mais difíceis de desnaturar e frequentemente indicam áreas 
reguladoras de genes (Ilhas CpG). Calcular esse índice é obrigatório ao desenhar 
primers de PCR para garantir que eles se conectem ao alvo na temperatura correta.

Solução Computacional:
Este script cria um 'Parser' (interpretador) nativo para o formato FASTA, o padrão 
universal de bancos genômicos. Utiliza dicionários (Hash Maps) para armazenar IDs 
como chaves e concatenar sequências genômicas multilinhas. O cálculo da porcentagem 
de GC é feito de forma iterativa, mantendo o controle do valor máximo encontrado com 
complexidade de tempo O(n).
"""

def extrair_maior_gc(dados_fasta):
    # 1. PARSER DE FASTA: Transforma o texto bruto num dicionário estruturado
    banco_genomas = {}
    id_atual = ""
    
    # O split('\n') quebra o texto linha por linha para o Python ler
    for linha in dados_fasta.strip().split('\n'):
        linha = linha.strip() # Limpa espaços ocultos
        if linha.startswith(">"):
            id_atual = linha[1:] # Pega o ID, ignorando o caractere '>'
            banco_genomas[id_atual] = ""
        else:
            banco_genomas[id_atual] += linha # Concatena a fita se ela tiver várias linhas
            
    # 2. CÁLCULO E COMPARAÇÃO
    id_campeao = ""
    maior_gc = 0.0
    
    for id_seq, sequencia in banco_genomas.items():
        # Conta C e G, divide pelo tamanho total da fita e multiplica por 100
        total_gc = sequencia.count('C') + sequencia.count('G')
        porcentagem_gc = (total_gc / len(sequencia)) * 100
        
        # Atualiza o pódio se encontrar um valor maior
        if porcentagem_gc > maior_gc:
            maior_gc = porcentagem_gc
            id_campeao = id_seq
            
    return id_campeao, maior_gc

# Bloco de execução (Simulação do Rosalind)
entrada_rosalind = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

id_result, gc_result = extrair_maior_gc(entrada_rosalind)

# O formato exigido pelo site: ID na primeira linha, número na segunda (com até 6 casas decimais)
print(id_result)
print(f"{gc_result:.6f}")
