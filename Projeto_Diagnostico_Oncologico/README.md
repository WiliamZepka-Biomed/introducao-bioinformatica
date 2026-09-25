# 🧬 Pipeline Secundário: Filtragem Clínica de Variantes (VCF)

## 📌 Objetivo Clínico
Transformar dados brutos de sequenciamento de nova geração (NGS) em laudos médicos acionáveis. Este projeto automatiza a ingestão de arquivos `.vcf` (Variant Call Format), aplica filtros de controle de qualidade e cruza as mutações do paciente com bancos de dados globais de patologia (ClinVar) para identificar alvos terapêuticos diretos em oncologia de precisão.

## 🛠️ Arquitetura e Ferramentas
* **Linguagem:** Python 3
* **Bibliotecas:** Pandas (Processamento escalável de DataFrames e matrizes clínicas).
* **Inputs:** Arquivos VCF (saída bruta de alinhadores como BWA/GATK) e tabelas clínicas (ClinVar).
* **Outputs:** Relatório estruturado contendo apenas variantes patogênicas de alta confiabilidade.

## 🔬 Lógica de Processamento
1. **Ingestão de Dados (Data Ingestion):** Leitura otimizada de laudos textuais massivos.
2. **Controle de Qualidade (QC):** Remoção rigorosa de artefatos de sequenciamento e ruídos de leitura da máquina (Phred QUAL < 30), eliminando falsos positivos no laudo médico.
3. **Anotação Clínica (Relational Merge):** Cruzamento de dados (via Cromossomo e Posição) entre as variantes detectadas no paciente e o histórico de patogenicidade global.
4. **Triagem Terapêutica:** Filtragem condicional isolando exclusivamente mutações classificadas como "Patogênicas", formatando a saída para avaliação do médico geneticista/oncologista.

## 👨‍🔬 Impacto no Negócio e na Rotina Laboratorial
A automação desta etapa substitui a busca manual de variantes em literatura médica. O script reduz o tempo de curadoria de horas para segundos por paciente, reduzindo o custo operacional do laboratório e o tempo de entrega do diagnóstico oncológico.
