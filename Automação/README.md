# Automação
## Documentações importantes
### [📄](https://selenium-python.readthedocs.io/) Selenium
Para automação web e scraping de dados.
### [📄](https://pyautogui.readthedocs.io/en/latest/) PyAutoGUI
Para manipulação de interface gráfica e automação desktop.

## Arquivos

### Navigations
Arquivo de navegação WEB e Desktop com diversas funções para manipulação do browser e janela.

#### Bibliotecas
As bibliotecas utilizadas são: selenium para manipulação WEB, pyautogui para manipulação Desktop, time e sys para auxílio.

> selenium, pyautogui, sys, time

#### WEB
  > #### WBrowser
  > chrome_browser(*site, *headless=False*, maximized=True*)
   > > Faz a configuração do Browser para ser utilizado, abrindo o navegador através da passagem do caminho do *chrome* e *chromedriver*.
   > > 
   > > Requere a passagem por parâmetro do site à ser aberto, opção de rodar em segundo plano com *headless* e a opção de abrir maximizado (padrão), através do *maximized*.
   > > 
   > > Retorna o ***driver*** para navegação.
