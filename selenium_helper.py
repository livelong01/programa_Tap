# selenium_helper.py

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def iniciar_navegador():
    # options = Options()
    # options.add_argument("--headless")  # Modo sem interface
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome()  #options=options 
    navegador.maximize_window()
    return navegador


def esperar_elemento_ID(navegador, valor, timeout=10):
    return WebDriverWait(navegador, timeout).until(
        EC.element_to_be_clickable((By.ID, valor)))


def esperar_elemento_XPATH(navegador, valor, timeout=10):
    return WebDriverWait(navegador, timeout).until(
        EC.element_to_be_clickable((By.XPATH, valor)))

def localizar_elemento_XPATH(navegador, valor, timeout=10):
    return WebDriverWait(
            navegador, timeout).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    valor)))

def localizar_elementos_XPATH(navegador, valor, timeout=10):    
    return WebDriverWait(
            navegador, timeout).until(
                EC.presence_of_all_elements_located((
                    By.XPATH,
                    valor)))



def preencher_inputs(list_ID, list_local, list_XPATH, navegador):
    for id, local, xpath in zip(list_ID, list_local, list_XPATH):
        # Clicar no input de origem/destino
        local_input = esperar_elemento_ID(navegador, id)
        local_input.click()
        local_input.clear()

        # Digitar "localizacao" no campo
        for letter in local:
            local_input.send_keys(letter)
            time.sleep(0.1)  # Simula digitação humana
        time.sleep(2)
        local_input.send_keys(Keys.BACKSPACE)

        primeira_opcao = esperar_elemento_XPATH(navegador, xpath)
        primeira_opcao.click()

def clicar_botao_calendario(navegador, xpath):
    try:
        # Aguardar até o botão estar clicável
        botao_calendario = esperar_elemento_XPATH(navegador, xpath)

        # Clicar no botão do calendário
        botao_calendario.click()
        print("✅ Botão do calendário clicado!")

    except Exception as e:
        print(f"❌ Erro ao clicar no botão: {e}")



def selecionar_mes(mes_desejado, navegador, xpath, xpath_proximo):
    while True:
        # Capturar o primeiro mês visível no calendário
        mes_visivel = localizar_elemento_XPATH(navegador, xpath).text
        print(f"Mês visível: {mes_visivel}")

        # Verifica se o mês visível é o que queremos
        if mes_desejado in mes_visivel:
            break  # Se encontrar, sai do loop

        # Caso contrário, clica no botão para avançar os meses
        botao_avancar = esperar_elemento_XPATH(navegador, xpath_proximo)
        botao_avancar.click()
        time.sleep(2)  # Pequena pausa para garantir que o calendário carregue