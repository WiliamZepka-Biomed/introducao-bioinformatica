"""
PIPELINE SECUNDÁRIO: FILTRAGEM CLÍNICA DE VARIANTES (VCF PARA LAUDO)

Contexto Biológico:
O pipeline primário (BWA/Samtools) gera um arquivo .vcf com milhares de variantes 
genéticas do paciente. A esmagadora maioria são mutações benignas ou artefatos de 
sequenciamento. O biomédico bioinformata precisa cruzar esses dados brutos com bancos 
de dados mundiais (ClinVar) para classificar o impacto biológico (Patogênico, Benigno, VUS) 
e entregar ao médico apenas o alvo terapêutico.

Solução Computacional:
O script utiliza Pandas para ingerir e estruturar dados do formato VCF. Aplica 
filtros de controle de qualidade (Phred QUAL > 30) para eliminar falsos positivos da 
máquina e realiza um 'merge' (cruzamento relacional de tabelas) com a base clínica, 
retornando um DataFrame final pronto para emissão de laudo.
"""

import pandas as pd
import io

# 1. SIMULAÇÃO DO ARQUIVO VCF (Saída bruta do seu pipeline)
# Colunas padrão: Cromossomo, Posição, ID, Base_Referência, Base_Paciente, Qualidade
vcf_bruto = """CHROM\tPOS\tID\tREF\tALT\tQUAL
chr17\t41196312\t.\tG\tA\t25.5
chr17\t41276045\t.\tC\tT\t99.9
chr13\t32914437\t.\tT\tC\t15.0
chr13\t32914438\t.\tG\tT\t85.2"""

# 2. SIMULAÇÃO DO BANCO DE DADOS CLÍNICO (Ex: ClinVar)
clinvar_db = """CHROM\tPOS\tGene\tImpacto
chr17\t41196312\tBRCA1\tBenigno
chr17\t41276045\tBRCA1\tPatogenico
chr13\t32914438\tBRCA2\tPatogenico"""

# Carrega os textos como DataFrames do Pandas
df_paciente = pd.read_csv(io.StringIO(vcf_bruto), sep='\t')
df_clinvar = pd.read_csv(io.StringIO(clinvar_db), sep='\t')

# 3. CONTROLE DE QUALIDADE (O olhar do Biomédico)
# Elimina mutações com Qualidade (QUAL) menor que 30 (baixa confiança do sequenciador)
df_paciente_filtrado = df_paciente[df_paciente['QUAL'] >= 30.0]

# 4. CRUZAMENTO DE DADOS (MERGE)
# Junta o genoma do paciente com o banco de dados clínico usando Cromossomo e Posição como chaves
laudo_final = pd.merge(df_paciente_filtrado, df_clinvar, on=['CHROM', 'POS'])

# 5. FILTRO FINAL DE LAUDO
# Mantém apenas o que é alvo de tratamento médico
alvos_terapeuticos = laudo_final[laudo_final['Impacto'] == 'Patogenico']

print("--- LAUDO ONCOLÓGICO FINAL ---")
print(alvos_terapeuticos[['Gene', 'CHROM', 'POS', 'REF', 'ALT', 'Impacto']])
