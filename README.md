# Programa TAP - Monitoramento de Preços de Passagens

Este projeto utiliza **Python** e **Selenium** para monitorar preços de passagens aéreas no site da TAP e enviar notificações via Telegram.
Observação_1: Esse projeto só funciona no trajeto Porto(Portugal) x Rio de Janeiro(Brasil)
Observação_2: Para funcionar os meses precisam ser iguais ou sequentes, por exemplo: (junho-julho).

## Funcionalidades
- Acessa o site da TAP e preenche os dados de origem, destino e datas.
- Busca os preços de ida e volta.
- Envia uma mensagem no Telegram caso o preço mude.

## Tecnologias Utilizadas
- Python
- Selenium
- Telegram Bot API
- dotenv para variáveis de ambiente

## Configuração
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/programa-tap.git
   cd programa-tap
   ```

## Estrutura do Projeto
```
programa_tap/
│
├── main.py            # Arquivo principal do programa
├── config.py          # Configurações do programa
├── selenium_helper.py # Funções auxiliares para Selenium
├── scraper.py         # Funções de scraping
├── utilities.py       # Funções utilitárias
├── .env.example       # Exemplo de arquivo .env
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

---
MIT License

Copyright (c) 2025 Jonathan Alonso Marques

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

