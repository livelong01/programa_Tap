# import time
import config
from selenium_helper import (
    iniciar_navegador,
    esperar_elemento_ID,
    preencher_inputs,
    clicar_botao_calendario,
    selecionar_mes)
from scraper import selecionar_dia
from utilities import soma, esperar
from telegram_mybot import enviar_telegram


def acessar_site(navegador):
    navegador.get(config.URL)
    botao_cookie = esperar_elemento_ID(navegador, config.COOKIE)
    botao_cookie.click()
    esperar()


def preencher_dados(navegador):
    preencher_inputs(config.ID, config.LOCAL, config.XPATH_LOCAL, navegador)
    esperar()
    clicar_botao_calendario(navegador, config.XPATH_BOTAO_CALENDARIO)
    esperar()
    selecionar_mes(config.MES_IDA, navegador, config.XPATH_MES,
                   config.XPATH_BOTAO_PROXIMO)


def buscar_precos(navegador):
    preco_ida = selecionar_dia(navegador, config.DIA_IDA,
                               config.XPATH_BOTOES_IDA, "ida")
    esperar()
    if config.MES_IDA != config.MES_VOLTA:
        preco_volta = selecionar_dia(navegador,
                                     config.DIA_VOLTA,
                                     config.XPATH_BOTOES_VOLTA, "volta")
    else:
        preco_volta = selecionar_dia(navegador, 
                                     config.DIA_VOLTA, 
                                     config.XPATH_BOTOES_IDA, "volta")
    esperar()
    return soma(preco_ida, preco_volta)


def enviar_mensagem(total):
    mensagem = (
        f"🛫 Ida: {config.DIA_IDA}/{config.MES_IDA}\n"
        f"🛬 Volta: {config.DIA_VOLTA}/{config.MES_VOLTA}\n"
        f"💰 Preço Total: R$ {total}"
    )
    enviar_telegram(config.TOKEN_BOT, config.CHAT_ID, mensagem)


total_anterior = 0.0  # variável global para armazenar o preço anterior


def executar_busca():
    global total_anterior  # usar a variável global
    navegador = iniciar_navegador()
    total = None
    try:
        acessar_site(navegador)
        preencher_dados(navegador)
        total = buscar_precos(navegador)
        if total == total_anterior:
            print("🔄 O preço não mudou.")
        else:
            enviar_mensagem(total)
            total_anterior = total
            print("✅ O preço mudou! Mensagem enviada.")     
    finally:
        navegador.quit()


if __name__ == "__main__":
    while True:
        try:
            executar_busca()
            print(f"✅ Busca finalizada! Aguardando {config.TEMPO_EM_HORAS}"
                  "hora(s) até a próxima execução...\n")
            esperar(config.TEMPO_EM_HORAS * 3600)
        except Exception as e:
            print(f"❌ Ocorreu um erro: {e}")