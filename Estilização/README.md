# Estilização

Informações relevantes de estilização para desenvolvimento de aplicações em Python.

> [!NOTE]
> Bibliotecas de automação: [Link](https://github.com/ESAran/Biblioteca-Python/tree/main#automa%C3%A7%C3%B5es "Bibliotecas")


## Trechos de códigos 

### Coloração de print() no console

```python
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + 'Hello, World!' + color.END)

```

![1710429164608](image/README/1710429164608.png)
