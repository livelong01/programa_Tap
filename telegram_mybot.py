# telegram.py
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

