import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


while True:
    # Configurações do Chrome
    options = Options()
    options.add_argument("--headless")  # Ativa o modo headless
    options.add_argument("--disable-gpu")  # Recomendado para Windows
    options.add_argument("--window-size=1920,1080")  # Tamanho da janela virtual
    options.add_argument("--no-sandbox")  # Pode ajudar em servidores Linux
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas em containers Linux


    # Abrir o navegador
    navegador = webdriver.Chrome(options=options) #options=options
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
    MES_IDA = "julho"
    DIA_IDA = "15"

    MES_VOLTA = "agosto"
    DIA_VOLTA = "1"

    #Função para selecionar uma data
    def selecionar_mes(mes_desejado):
        while True:
            # Capturar o primeiro mês visível no calendário
            mes_visivel = WebDriverWait(
                navegador, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        "//div[@role='presentation' "
                        "and contains(@class, 'text-sm font-medium')]"))).text
            print(f"Mês visível: {mes_visivel}")
            
            # Verifica se o mês visível é o que queremos
            if mes_desejado in mes_visivel:
                break  # Se encontrar, sai do loop
            
            # Caso contrário, clica no botão para avançar os meses
            botao_avancar = WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//button[@name='next-month']")))
            botao_avancar.click()
            time.sleep(2)  # Pequena pausa para garantir que o calendário carregue

    def selecionar_dia_ida(dia_desejado):
        preco_ida = None
        botoes_dia = WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[@name='day']"))
        )

        for botao in botoes_dia:
            try:
                numero_dia = botao.find_element(By.XPATH, ".//span[1]").text.strip()
                preco_elemento = botao.find_elements(By.XPATH, ".//span[2]")  
                preco = preco_elemento[0].text.strip().replace("R$", "").replace("\u00a0", "").replace(".", "").replace(",", ".") if preco_elemento else "N/A"


                if numero_dia == str(dia_desejado):
                    print(f"✅ Selecionando o dia {dia_desejado} com preço {preco}")
                    botao.click()
                    preco_ida = preco
                    break

            except Exception as e:
                print(f"Erro ao processar um botão de dia: {e}")
        return preco_ida
        
    def selecionar_dia_volta(dia_volta):
        preco_volta = None
        try:
            # Captura todos os botões do segundo mês (normalmente o da volta)
            botoes_dia = WebDriverWait(navegador, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "(//button[@name='day'])[position() > last() div 2]"))
            )

            for botao in botoes_dia:
                try:
                    numero_dia = botao.find_element(By.XPATH, ".//span[1]").text.strip()

                    preco_elemento = botao.find_elements(By.XPATH, ".//span[2]")  
                    preco = preco_elemento[0].text.strip().replace("R$", "").replace("\u00a0", "").replace(".", "").replace(",", ".") if preco_elemento else "N/A"


                    if numero_dia == str(dia_volta):
                        print(f"✅ Dia {dia_volta} encontrado no segundo mês com preço {preco}")
                        preco_volta = preco
                        break

                except Exception as e:
                    print(f"Erro ao processar um botão de dia: {e}")

            return preco_volta

        except Exception as e:
            print(f"❌ Erro ao tentar capturar os dias do segundo mês: {e}")
            return None


    import requests


    def enviar_telegram(token, chat_id, mensagem):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": mensagem
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Mensagem enviada com sucesso para o Telegram!")
        else:
            print(f"❌ Erro ao enviar mensagem: {response.text}")


    # teste de seleção de mês e dia
    TEMPO_EM_HORAS = 0.01


    try:
        selecionar_mes(MES_IDA)
        time.sleep(2)

        preco_ida = selecionar_dia_ida(DIA_IDA)
        time.sleep(2)
        preco_volta = selecionar_dia_volta(DIA_VOLTA)

        if preco_ida and preco_volta:
            total = float(preco_ida) + float(preco_volta)
            print(f"💸 Preço total: R$ {total:.2f}")

        token_bot = "7642050445:AAE71v4HmLQJYrmKA8TREzyXHfhV9BgH3KU"
        chat_id = "6439519803"
        mensagem = f"Preço ida: R$ {preco_ida} dia {DIA_IDA} do mes {MES_IDA} \nPreço volta: R$ {preco_volta} dia {DIA_VOLTA} do mes {MES_VOLTA}\nTotal: R$ {total}"
        enviar_telegram(token_bot, chat_id, mensagem)

        navegador.quit()
        print(f"✅ Busca finalizada! Aguardando {TEMPO_EM_HORAS} hora(s) até a próxima execução...\n")
        time.sleep(TEMPO_EM_HORAS * 3600)

    except Exception as erro:
        print(f"❌ Erro geral: {erro}")
        navegador.quit()
        print(f"⏱️ Tentando novamente em {TEMPO_EM_HORAS} hora(s)...")
        time.sleep(TEMPO_EM_HORAS * 3600)