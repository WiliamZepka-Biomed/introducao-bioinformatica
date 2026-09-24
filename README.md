# Pipeline Primário de Genômica de Precisão 🧬

## 📌 Objetivo Clínico
Este projeto automatiza a identificação de mutações genéticas (Variant Calling) a partir de dados brutos de sequenciamento de nova geração (NGS). O objetivo é simular o fluxo de processamento de um laboratório de diagnóstico molecular, transformando dados brutos da máquina em um laudo clínico apontando a mutação.

## 🛠️ Ferramentas Utilizadas (Stack Bioinformática)
* **Fastp:** Controle de qualidade e remoção de lixo de sequenciamento (Trimming).
* **BWA (Burrows-Wheeler Aligner):** Mapeamento e alinhamento contra o genoma de referência.
* **Samtools:** Compressão e ordenação de dados genômicos (conversão SAM > BAM).
* **Bcftools:** Análise estatística e chamada de variantes (Variant Calling / VCF).

## 🔬 Fluxo de Trabalho
1. **Entrada:** Leitura do DNA do paciente em formato `.fastq`.
2. **Filtragem:** Corte de bases com baixo *Phred Score* para evitar falsos positivos clínicos.
3. **Alinhamento:** Reconstrução da sequência posicionando as leituras limpas sobre o genoma oficial.
4. **Diagnóstico:** Identificação de *mismatches* (diferenças entre o paciente e a referência), gerando o laudo final em formato `.vcf`.

## 👨‍🔬 Sobre o Autor
Biomédico em reta final de formação, aplicando conhecimentos de genética, biologia molecular e patologia clínica na automação e análise de dados biológicos. Foco em unir a precisão da biologia com a escalabilidade da computação.
