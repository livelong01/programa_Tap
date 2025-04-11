#Scraper.py
from selenium_helper import (localizar_elementos_XPATH)
from selenium.webdriver.common.by import By

def selecionar_dia(navegador, dia_desejado, xpath_botoes, descricao=""):
    preco = None
    try:
        botoes_dia = localizar_elementos_XPATH(navegador, xpath_botoes)

        for botao in botoes_dia:
            try:
                numero_dia = botao.find_element(By.XPATH, ".//span[1]").text.strip()
                preco_elemento = botao.find_elements(By.XPATH, ".//span[2]")  
                preco_texto = preco_elemento[0].text.strip().replace("R$", "").replace("\u00a0", "").replace(".", "").replace(",", ".") if preco_elemento else "N/A"

                if numero_dia == str(dia_desejado):
                    print(f"✅ Selecionando o dia {dia_desejado} {descricao} com preço {preco_texto}")
                    botao.click()
                    preco = preco_texto
                    break

            except Exception as e:
                print(f"Erro ao processar um botão de dia: {e}")

    except Exception as e:
        print(f"❌ Erro ao tentar capturar os dias {descricao}: {e}")

    return preco



