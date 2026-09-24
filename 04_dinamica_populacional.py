"""
DINÂMICA POPULACIONAL E PROGRAMAÇÃO DINÂMICA (FIBONACCI MODIFICADO)

Contexto Biológico:
O crescimento populacional e a hereditariedade são fundamentos da genética de
populações. Na bioinformática, este problema introduz a base matemática da 
'Programação Dinâmica'. Este é o exato princípio algorítmico utilizado por 
softwares de alinhamento global e local de sequências genômicas (como 
Needleman-Wunsch e Smith-Waterman) para comparar milhares de fitas de DNA 
simultaneamente sem esgotar a memória RAM do servidor.

Solução Computacional:
Uma abordagem recursiva simples criaria uma árvore de cálculos redundante,
travando a máquina para números altos. O algoritmo utiliza Programação Dinâmica 
(abordagem bottom-up), iterando sobre os meses e armazenando na memória
apenas os dados das duas últimas gerações. Isso reduz a complexidade espacial 
para O(1) e a complexidade temporal para O(n).
"""

def calcular_populacao_coelhos(meses, ninhada):
    # Condição inicial de Fibonacci: Nos meses 1 e 2, existe apenas 1 par
    if meses == 1 or meses == 2:
        return 1
    
    # Variáveis armazenando o passado (Programação Dinâmica)
    geracao_anterior = 1     # F(n-1)
    geracao_reprodutora = 1  # F(n-2)
    
    # Calcula a partir do mês 3 até o mês alvo
    for _ in range(3, meses + 1):
        # A nova geração = quem já estava vivo + filhos gerados pelos adultos
        populacao_atual = geracao_anterior + (geracao_reprodutora * ninhada)
        
        # Atualiza o tempo: o mês passado vira o mês retrasado para o próximo ciclo
        geracao_reprodutora = geracao_anterior
        geracao_anterior = populacao_atual
        
    return geracao_anterior

# Bloco de execução (Simulação do Rosalind)
# O Rosalind sempre fornece os números em uma linha, separados por espaço
entrada_rosalind = "5 3"

# A função split() separa o texto onde tem espaço, e map(int) converte para número
n, k = map(int, entrada_rosalind.split())

resultado = calcular_populacao_coelhos(meses=n, ninhada=k)
print(f"População final após {n} meses: {resultado} pares de coelhos.")
