import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Abrir o navegador
navegador = webdriver.Chrome()
navegador.get("https://www.flytap.com/pt-br")
navegador.maximize_window()
time.sleep(3)

# Aceitar o cookie
botao_cookie = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
)
botao_cookie.click()
time.sleep(2)

ID_ORIGEM = ":R56m6r9mH2:"
ORIGEM = " Porto"
XPATH_ORIGEM = "//div[@data-value='OPO']"

ID_DESTINO = ":R5em6r9mH2:"
DESTINO = "rio de janeiro"
XPATH_DESTINO = "//div[@data-value='RIO']"

ID = [ID_ORIGEM, ID_DESTINO]
LOCAL = [ORIGEM, DESTINO]
XPATH_LOCAL = [XPATH_ORIGEM, XPATH_DESTINO]

for id, local, xpath in zip(ID, LOCAL, XPATH_LOCAL):
    # Clicar no input de origem/destino
    local_input = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, id))  # Pode precisar ajustar esse ID
    )
    local_input.click()
    local_input.clear()

    # Digitar "Porto" no campo

    for letter in local:
        local_input.send_keys(letter)
        time.sleep(random.uniform(0.1, 0.3))  # Simula digitação humana

    time.sleep(2)  # Tempo para o menu suspenso carregar

    # Selecionar a opção correta do menu suspenso pelo código do aeroporto (OPO) ou nome
    primeira_opcao = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    primeira_opcao.click()

# Esperar um tempo para visualizar o resultado
time.sleep(5)


# Novo XPath do botão do calendário
xpath_botao_calendario = "//div[contains(@class, 'flex') and contains(@aria-haspopup, 'dialog')]/button"

try:
    # Aguardar até o botão estar clicável
    botao_calendario = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_botao_calendario))
    )

    # Clicar no botão do calendário
    botao_calendario.click()
    print("✅ Botão do calendário clicado!")

except Exception as e:
    print(f"❌ Erro ao clicar no botão: {e}")


# Definir datas desejadas
MES_IDA = "Junho 2024"
DIA_IDA = "15"

MES_VOLTA = "Julho 2024"
DIA_VOLTA = "5"

# Tempo para verificar visualmente
time.sleep(20)
navegador.quit()