#funcao Soma
from time import sleep


def soma(preco_ida, preco_volta):  
    try:
        # Converte os preços para float, tratando o caso em que o preço é "N/A"
        preco_ida_float = float(preco_ida) if preco_ida != "N/A" else 0.0
        preco_volta_float = float(preco_volta) if preco_volta != "N/A" else 0.0
        
        # Calcula a soma dos preços
        total = preco_ida_float + preco_volta_float
        
        return total
    
    except ValueError as e:
        print(f"Erro ao converter os preços: {e}")
        return None 


def esperar(segundos=2.0):
    sleep(segundos)