# Automação de Cadastro de Produtos

Projeto de automação em Python que realiza o cadastro automático de produtos em um sistema web utilizando **PyAutoGUI** e leitura de dados a partir de um arquivo **CSV**.

---

# 📌 Funcionalidades

* Abrir navegador automaticamente
* Fazer login no sistema
* Ler dados de produtos a partir de um arquivo CSV
* Preencher formulários automaticamente
* Cadastrar múltiplos produtos sem intervenção manual

---

# 🗂 Estrutura do Projeto

```
automacao_cadastro/

│
├── main.py               # Arquivo principal que inicia a automação
├── config.py             # Configurações do projeto (login, URL, etc)
├── navegador.py          # Funções para abrir o navegador
├── cadastro.py           # Lógica de cadastro dos produtos
├── auxiliar_mouse.py     # Utilitário para descobrir coordenadas do mouse
├── requirements.txt      # Dependências do projeto
│
└── data/
    └── produtos.csv      # Base de dados com produtos
```

---

# ⚙️ Requisitos

Python 3.8 ou superior.

Bibliotecas utilizadas:

* pyautogui
* pandas

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

# 🚀 Como executar

1. Abra o terminal dentro da pasta do projeto

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute o programa:

```
python main.py
```

O sistema irá:

1. Abrir o navegador
2. Acessar o site
3. Fazer login
4. Cadastrar automaticamente todos os produtos do arquivo CSV

---

# 📄 Estrutura do CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

```
codigo
marca
tipo
categoria
preco_unitario
custo
obs
```

Exemplo:

```
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Logitech,Mouse,Periféricos,120,70,
002,Dell,Teclado,Periféricos,200,120,ABNT2
```

---

# 🖱 Descobrir coordenadas do mouse

Caso precise ajustar posições do clique na tela:

Execute:

```
python auxiliar_mouse.py
```

Depois posicione o mouse no local desejado e aguarde 5 segundos.

O programa mostrará a posição do cursor.

---

# ⚠️ Observações

* A automação depende da posição dos elementos na tela.
* Recomenda-se usar resolução de tela padrão.
* Não utilize o computador enquanto a automação estiver rodando.

---

# 🔧 Melhorias futuras

* Automação usando **Selenium (mais estável)**
* Interface gráfica
* Logs de execução
* Sistema de pausa e retomada
* Executável `.exe`

---

# 👨‍💻 Autor

Projeto desenvolvido para automação de cadastro de produtos utilizando Python.
