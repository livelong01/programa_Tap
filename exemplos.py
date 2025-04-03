# selecionar o elemento origem na tela:
botao_origem = navegador.find_element("class name", "botao-verde")

# clicar em um elemento
botao_origem.find_element("id", "firstname").send_keys("Lira")

# encontrar varios elementos
lista_botoes = navegador.find_elements("class name", "header__titulo")

for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

# selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

# navegar para um site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# escrever em um campo/formulario
navegador.find_element("id", "firstname").send_keys("Lira")
navegador.find_element("id", "email").send_keys("pythonimpressionador@gmail.com")
navegador.find_element("id", "phone").send_keys("2199999999")

botao_quero_clicar = navegador.find_element("id", "_form_2475_submit")

# dar scroll (colocar um elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         botao_quero_clicar)

# opcao 1 - espera manual
# time.sleep(3)

# opcao 2 - espera dinâmica
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)
espera.until(EC.element_to_be_clickable(botao_quero_clicar))

botao_quero_clicar.click()
time.sleep(10)






# Função para selecionar uma data
def selecionar_data(mes_desejado, dia_desejado):
    while True:
        # Capturar os meses visíveis no calendário
        meses_visiveis = navegador.find_elements(By.XPATH, "//div[contains(@class, 'calendar-month-label')]")
        
        # Verifica se um dos meses exibidos é o que queremos
        if any(mes_desejado in mes.text for mes in meses_visiveis):
            break  # Se encontrar, sai do loop
        
        # Caso contrário, clica no botão para avançar os meses
        botao_avancar = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'next-month')]"))
        )
        botao_avancar.click()
        time.sleep(2)  # Pequena pausa para garantir que o calendário carregue

    # Selecionar o dia desejado dentro do mês correto
    dia = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[text()='{dia_desejado}']"))
    )
    dia.click()


# Selecionar a data de ida
selecionar_data(MES_IDA, DIA_IDA)
time.sleep(2)

# Selecionar a data de volta
selecionar_data(MES_VOLTA, DIA_VOLTA)
time.sleep(2)

botao_confirmar.click()