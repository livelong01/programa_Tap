from selenium_helper import (
    iniciar_navegador,
    esperar_elemento_ID,
    preencher_inputs,
    clicar_botao_calendario,
    selecionar_mes,
)
from scraper import (
    selecionar_dia,
)
import config
import time
import soma_preco
from telegram_mybot import enviar_telegram


while True:
    # Iniciar o navegador
    navegador = iniciar_navegador()
    navegador.get(config.URL) # Acessar a URL da Tap

    # Aceitar o cookie
    botao_cookie = esperar_elemento_ID(navegador, config.COOKIE)
    botao_cookie.click()
    time.sleep(2) 

    # Preencher os campos de origem e destino
    preencher_inputs(config.ID, config.LOCAL, config.XPATH_LOCAL, navegador)
    time.sleep(2)

    # Clicar no botão do calendário
    clicar_botao_calendario(navegador, config.XPATH_BOTAO_CALENDARIO)
    time.sleep(2)

    # Econtrar o par de meses correto
    selecionar_mes(config.MES_IDA, navegador, config.XPATH_MES,
                   config.XPATH_BOTAO_PROXIMO)    
    
    # Selecionar o dia de ida
    preco_ida = selecionar_dia(navegador, config.DIA_IDA, config.XPATH_BOTOES_IDA, "ida")
    time.sleep(2)
    # Selecionar o dia de volta
    preco_volta = selecionar_dia(navegador, config.DIA_VOLTA, config.XPATH_BOTOES_VOLTA, "volta")
    time.sleep(2)

    # somar os preços
    total = soma_preco.soma(preco_ida, preco_volta)

    # Mensagem para o bot
    mensagem = mensagem = (
        f"🛫 Ida: {config.DIA_IDA}/{config.MES_IDA}\n"
        f"🛬 Volta: {config.DIA_VOLTA}/{config.MES_VOLTA}\n"
        f"💰 Preço Total: R$ {total}"
    )
    
    # Enviar mensagem para o Telegram
    enviar_telegram(config.TOKEN_BOT, config.CHAT_ID, mensagem)

    # Fechar o navegador e aguardar o tempo definido
    navegador.quit()
    print(f"✅ Busca finalizada! Aguardando {config.TEMPO_EM_HORAS} hora(s) até a próxima execução...\n")
    time.sleep(config.TEMPO_EM_HORAS * 3600)
