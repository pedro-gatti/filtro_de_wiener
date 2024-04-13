import numpy as np

class Wiener:
    def __init__(self, sinal_ruidoso, sinal_limpo, estimador):
        self.sinal_ruidoso = sinal_ruidoso
        self.sinal_limpo = sinal_limpo
        self.estimador = estimador
        
    def montar_matriz_A(self):
    
        # inicializando a matriz_A   
        matriz_A = []
        
        # monta a matriz_A dividindo o vetor do sinal_ruidoso de acordo com o valor do estimador
        for i in range(0, len(self.sinal_ruidoso), 1):
            linha = self.sinal_ruidoso[i:i+self.estimador]
            # se a linha tirada do vetor sinal_ruidoso for menor que o tamanho do estiamdor, retorna a matriz_A
            if len(linha)==self.estimador:
                matriz_A.append(linha)
            else:
                return matriz_A
    
    def montar_matriz_B(self):

        # inicializando a matriz_B 
        matriz_B = []

        # passa os valores do vetor sinal_limpo para a matriz_B
        for i in range(0, len(self.sinal_limpo)):
            linha = self.sinal_limpo[i]
            matriz_B.append(linha)

        return matriz_B
    
    def imprimir_matriz(self, matriz_qualquer):
        for valor in matriz_qualquer:
            print(valor)

    def achar_transposta(self, matriz_original):
        
        # inicializando a matriz transposta (uma lista de listas) vazia
        matriz_transposta = []
        for i in range(len(matriz_original[0])):
            matriz_transposta.append([])
        
        # adiciona a posição [i, j] da matriz_original na posição [j, i] da matriz_transposta  
        for i in range (len(matriz_original)):
            for j in range (len(matriz_original[0])):
                matriz_transposta[j].append(matriz_original[i][j])
        
        return matriz_transposta   
        
    def encontrar_erro(self, vetor_resultado, vetor_aproximado):
        
        #inicializando o vetor de erros
        vetor_de_erros = []
        vetor_aproximado = vetor_aproximado.tolist()
        
        #calcula o erro medio entre o vetor de resultado e o vetor aptroximado
        for i in range(len(vetor_resultado)):
            erro = vetor_resultado[i] - vetor_aproximado[i]
            abs(erro)
            vetor_de_erros.append(erro)

        erro_medio = sum(vetor_de_erros)/len(vetor_de_erros)

        return erro_medio, vetor_de_erros
    
    def resolver_sistema(self):
        ########################################################
        # monta as matrizes a partir dos sinais
        
        matriz_A = self.montar_matriz_A()
        print('\n\t\tMatriz A:\n')
        self.imprimir_matriz(matriz_A)
        
        matriz_B = self.montar_matriz_B()
        print('\n\t\tMatriz B:\n')
        self.imprimir_matriz(matriz_B)
        
        ########################################################
        
        ########################################################
        # encontra a trasposta de A
        
        matriz_A_transposta = self.achar_transposta(matriz_A)
        print('\n\t\tMatriz A Transposta:\n')
        self.imprimir_matriz(matriz_A_transposta)
        
        ########################################################
        
        ########################################################
        # monta o novo sistema: At . A . (a, b, c) = At . B
        
        nova_matriz_sistema = np.dot(matriz_A_transposta, matriz_A)
        print('\n\t\tAt . A =\n')
        self.imprimir_matriz(nova_matriz_sistema)
        
        nova_matriz_resultado = np.dot(matriz_A_transposta, matriz_B)
        print('\n\t\tAt . B =\n')
        self.imprimir_matriz(nova_matriz_resultado)
        
        ########################################################
        
        ########################################################
        # resolve o novo sistema (solução aproximada)

        solucao_aproximada = np.linalg.solve(nova_matriz_sistema, nova_matriz_resultado)
        print('\n\t\tSolução Aproximada do Sistema:\n')
        self.imprimir_matriz(solucao_aproximada)
        
        ########################################################
        
        ########################################################
        # confere se o resultado bate com o exemplo e calcula o erro medio

        valores_aproximados = np.dot(matriz_A, solucao_aproximada)
        print('\n\t\tConferencia da Solução:\n')
        self.imprimir_matriz(valores_aproximados)
        
        erro_medio, vetor_de_erros = self.encontrar_erro(matriz_B, valores_aproximados)
        print(f'\n\t\tVetor de Erros:\n{vetor_de_erros}')
        print(f'\n\t\tErro Medio:\n{erro_medio}')
        
        ########################################################
        
        return solucao_aproximada, erro_medio, vetor_de_erros