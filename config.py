# config.py

TOKEN_BOT = "7642050445:AAE71v4HmLQJYrmKA8TREzyXHfhV9BgH3KU"
CHAT_ID = "6439519803"

URL = "https://www.flytap.com/pt-br"

COOKIE = "onetrust-accept-btn-handler"

ORIGEM = " Porto"
ID_ORIGEM = ":R56m6r9mH2:"
XPATH_ORIGEM = "//div[@data-value='OPO']"

DESTINO = "rio de janeiro"
ID_DESTINO = ":R5em6r9mH2:"
XPATH_DESTINO = "//div[@data-value='RIO']"

# Listas com fixos

ID = [ID_ORIGEM, ID_DESTINO]
LOCAL = [ORIGEM, DESTINO]
XPATH_LOCAL = [XPATH_ORIGEM, XPATH_DESTINO]

XPATH_BOTAO_CALENDARIO = "//div[contains(@class, 'flex') and contains(@aria-haspopup, 'dialog')]/button"
XPATH_MES = ("//div[@role='presentation' "
             "and contains(@class, 'text-sm font-medium')]")
XPATH_BOTAO_PROXIMO = "//button[@name='next-month']"

# datas :

MES_IDA = "julho"
DIA_IDA = "15"

MES_VOLTA = "agosto"
DIA_VOLTA = "1"

# xpaths para os dias
XPATH_BOTOES_IDA = ("//button[@name='day']")
XPATH_BOTOES_VOLTA = ("(//button[@name='day'])[position() > last() div 2]")

# tempo de espera em horas
TEMPO_EM_HORAS = 0.01