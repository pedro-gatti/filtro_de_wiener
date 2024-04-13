import numpy as np
from wiener import Wiener

def main():

    sinal_ruidoso = [1,2,3,4,5,6]
    sinal_limpo = [7,8,9,10]
    estimador = 3
    
    wiener = Wiener(sinal_ruidoso, sinal_limpo, estimador)
    
    solucao_aproximada, erro_medio, vetor_de_erros = wiener.resolver_sistema()
    
    print("\n\t\tSolução Aproximada do Sistema:")
    wiener.imprimir_matriz(solucao_aproximada)
    
    print("\n\t\tVetor de Erros:")
    print(vetor_de_erros)
    
    print("\n\t\tErro Médio:")
    print(erro_medio)
    
if __name__ == '__main__':
    main()