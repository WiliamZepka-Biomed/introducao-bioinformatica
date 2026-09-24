%%bash

# --- CONFIGURAÇÕES INICIAIS ---
REFERENCIA="referencia.fasta"
AMOSTRA="paciente.fastq"
NOME_SAIDA="paciente_001_automatizado"

echo "⏳ INICIANDO PIPELINE GENÔMICO PARA: $NOME_SAIDA"
echo "------------------------------------------------"

# 1. LIMPEZA
echo "[1/4] Limpando arquivo bruto..."
./fastp -i $AMOSTRA -o $NOME_SAIDA.fastq 2> /dev/null

# 2. ALINHAMENTO (Mapeamento)
echo "[2/4] Alinhando contra a referência..."
bwa mem -T 15 $REFERENCIA $NOME_SAIDA.fastq > $NOME_SAIDA.sam 2> /dev/null

# 3. CONVERSÃO E ORDENAÇÃO
echo "[3/4] Comprimindo SAM para BAM..."
samtools view -bS $NOME_SAIDA.sam > temp.bam 2> /dev/null
samtools sort temp.bam -o $NOME_SAIDA.bam 2> /dev/null
samtools index $NOME_SAIDA.bam 2> /dev/null
rm temp.bam $NOME_SAIDA.sam # Limpa os arquivos temporários pesados

# 4. DIAGNÓSTICO (Chamada de Variante)
echo "[4/4] Buscando mutações (VCF)..."
bcftools mpileup -f $REFERENCIA $NOME_SAIDA.bam 2> /dev/null | bcftools call -mv --ploidy 1 -O v -o $NOME_SAIDA.vcf 2> /dev/null

echo "------------------------------------------------"
echo "✅ PIPELINE CONCLUÍDO! RESULTADO CLÍNICO:"
cat $NOME_SAIDA.vcf | grep -v "^##"
