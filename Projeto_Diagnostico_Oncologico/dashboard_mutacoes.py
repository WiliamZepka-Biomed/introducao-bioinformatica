"""
GERADOR DE GRÁFICO CLÍNICO (DATA VIZ)

Contexto Biológico e Clínico:
Após a filtragem das variantes (VCF), o laboratório precisa mapear a incidência 
de mutações por gene para análise epidemiológica ou direcionamento de painéis 
oncológicos. Genes com alta taxa de mutação patogênica (como TP53 ou BRCA1) 
justificam o desenvolvimento de testes diagnósticos direcionados.

Solução Computacional:
O script utiliza a biblioteca Matplotlib integrada ao Pandas para converter 
dados tabulares em recursos visuais. A plotagem direta de gráficos de barras 
resume o volume de variantes deletérias por gene alvo, facilitando a tomada de 
decisão médica.
"""

import pandas as pd
import matplotlib.pyplot as plt
import io

# 1. SIMULAÇÃO DOS DADOS DO LAUDO (O resultado final do seu script anterior)
dados_consolidados = """Gene\tTotal_Mutacoes_Patogenicas
TP53\t85
BRCA1\t42
BRCA2\t28
EGFR\t15
PIK3CA\t64"""

# Carrega os dados para o Pandas
df_grafico = pd.read_csv(io.StringIO(dados_consolidados), sep='\t')

# 2. CONFIGURAÇÃO DO GRÁFICO
# Define o tamanho da imagem
plt.figure(figsize=(8, 5))

# Cria um gráfico de barras (eixo X = Genes, eixo Y = Quantidade de Mutações)
plt.bar(df_grafico['Gene'], df_grafico['Total_Mutacoes_Patogenicas'], color='darkred')

# Adiciona títulos e rótulos para o médico entender
plt.title('Frequência de Mutações Patogênicas por Gene Alvo', fontsize=14, fontweight='bold')
plt.xlabel('Gene', fontsize=12)
plt.ylabel('Frequência na Amostra', fontsize=12)

# Adiciona uma grade de fundo para facilitar a leitura dos números
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 3. GERAÇÃO DA IMAGEM
plt.show()
