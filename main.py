import numpy as np

def montar_matriz_A(sinal_ruidoso, estimador):
    
    # inicializando a matriz_A   
    matriz_A = []
    
    # monta a matriz_A dividindo o vetor do sinal_ruidoso de acordo com o valor do estimador
    for i in range(0, len(sinal_ruidoso), 1):
        linha = sinal_ruidoso[i:i+estimador]
        # se a linha tirada do vetor sinal_ruidoso for menor que o tamanho do estiamdor, retorna a matriz_A
        if len(linha)==estimador:
            matriz_A.append(linha)
        else:
            return matriz_A
    
def montar_matriz_B(sinal_limpo):

    # inicializando a matriz_B 
    matriz_B = []

    # passa os valores do vetor sinal_limpo para a matriz_B
    for i in range(0, len(sinal_limpo)):
        linha = sinal_limpo[i]
        matriz_B.append(linha)

    return matriz_B
    
def imprimir_matriz(matriz_qualquer):
    for valor in matriz_qualquer:
        print(valor)

def achar_transposta(matriz_original):
    
    # inicializando a matriz transposta (uma lista de listas) vazia
    matriz_transposta = []
    for i in range(len(matriz_original[0])):
        matriz_transposta.append([])
    
    # adiciona a posição [i, j] da matriz_original na posição [j, i] da matriz_transposta  
    for i in range (len(matriz_original)):
        for j in range (len(matriz_original[0])):
            matriz_transposta[j].append(matriz_original[i][j])
    
    return matriz_transposta
        

def main():

    sinal_ruidoso = [1,2,3,4,5,6]
    sinal_limpo = [7,8,9,10]
    estimador = 3
    
    ########################################################
    # monta as matrizes a partir dos sinais
    
    matriz_A = montar_matriz_A(sinal_ruidoso, estimador)
    print('\n\t\tMatriz A:\n')
    imprimir_matriz(matriz_A)
    
    matriz_B = montar_matriz_B(sinal_limpo)
    print('\n\t\tMatriz B:\n')
    imprimir_matriz(matriz_B)
    
    ########################################################
    
    ########################################################
    # encontra a trasposta de A
    
    matriz_A_transposta = achar_transposta(matriz_A)
    print('\n\t\tMatriz A Transposta:\n')
    imprimir_matriz(matriz_A_transposta)
    
    ########################################################
    
    ########################################################
    # monta o novo sistema: At . A . (a, b, c) = At . B
    
    nova_matriz_sistema = np.dot(matriz_A_transposta, matriz_A)
    print('\n\t\tAt . A =\n')
    imprimir_matriz(nova_matriz_sistema)
    
    nova_matriz_resultado = np.dot(matriz_A_transposta, matriz_B)
    print('\n\t\tAt . B =\n')
    imprimir_matriz(nova_matriz_resultado)
    
    ########################################################
    
    ########################################################
    # resolve o novo sistema (solução aproximada)

    solucao_aproximada = np.linalg.solve(nova_matriz_sistema, nova_matriz_resultado)
    print('\n\t\tSolução Aproximada do Sistema:\n')
    imprimir_matriz(solucao_aproximada)
    
    ########################################################
    
    ########################################################
    # confere se o resultado bate com o exemplo

    confere = np.dot(matriz_A, solucao_aproximada)
    print('\n\t\tConferencia da Solução:\n')
    imprimir_matriz(confere)
    
    ########################################################

if __name__ == '__main__':
    main()