import numpy as np

def montar_matriz_A(sinal_ruidoso, estimador):
       
    matriz_A = []
    
    for i in range(0, len(sinal_ruidoso), 1):
        linha = sinal_ruidoso[i:i+estimador]
        if len(linha)==3:
            matriz_A.append(linha)
        else:
            return matriz_A
    
    
def montar_matriz_B(sinal_limpo):

    matriz_B = []

    for i in range(0, len(sinal_limpo)):
        linha = sinal_limpo[i]
        matriz_B.append(linha)

    return matriz_B
    
def imprimir_matriz(matriz_qualquer):
    for valor in matriz_qualquer:
        print(valor)

def achar_transposta(matriz_original):
    
    matriz_transposta = [[linha[i] for linha in matriz_original] for i in range(len(matriz_original[0]))]
    
    return matriz_transposta
        

def main():

    sinal_ruidoso = [1,2,3,4,5,6]
    sinal_limpo = [7,8,9,10]
    estimador = 3
    x = []
    solucao = []
    
    matriz_A = montar_matriz_A(sinal_ruidoso, estimador)
    imprimir_matriz(matriz_A)
    
    matriz_B = montar_matriz_B(sinal_limpo)
    imprimir_matriz(matriz_B)
    
    matriz_A_transposta = achar_transposta(matriz_A)
    imprimir_matriz(matriz_A_transposta)
    
    nova_matriz_sistema = np.dot(matriz_A_transposta, matriz_A)
    imprimir_matriz(nova_matriz_sistema)
    
    nova_matriz_resultado = np.dot(matriz_A_transposta, matriz_B)
    imprimir_matriz(nova_matriz_resultado)

if __name__ == '__main__':
    main()