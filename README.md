<p align="center" style="margin: 40px 0">
    <img src="./doc-images/logo.svg" height="100px">
</p>

<div align="center">

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

</div>

# Learn with Me - API

Compartilhe seus estudos e aprenda com outras pessoas.

**Learn with Me** tem como objetivo conectar e ajudar pessoas a estudarem através do compartilhamento de conteúdos gratuitos na internet de forma estruturada e didática entre usuários. Venha estudar com a comunidade **Learn with Me** também! 😉

Projeto desenvolvido para o MVP na Sprint 1 da Pós Graduação de Engenharia de Software da PUC-Rio.

## Executando a API


### 1 - Clonando o repositório
Antes de tudo, precisamos clonar o projeto para ser executado em sua máquina. Você pode clonar esse repositório fazendo o download por meio de um arquivo ZIP ou através do seguinte comando:

```
    git clone https://github.com/MicaelRiboura/learn-with-me-api.git
```

> ⚠️ Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

#

Para executar a aplicação é necessário ter todas as libs (bibliotecas) python listadas no arquivo `requirements.txt` instaladas. 

#

### 2 - Criando um ambiente virtual (opcional)

Para a instalação das dependências da aplicação, é **fortemente recomendado** a criação de um ambiente virtual python. Esse ambiente tem como objetivo dar mais liberdade de utilizar diferentes bibliotecas e até versões da linguagem Python, sem que haja conflito entre elas.

Você pode criar um  ambiente virtual a partir do seguinte comando:

```
    python -m venv env
```

Após criar o ambiente virtual, você pode ativá-lo a partir do seguinte comando:

```
    # Windows:
    .\env\Scripts\activate.ps1

    # Linux ou Mac:
    source ./python_env/bin/activate
```

> ⚠️ Esse é um passo opcional, mas fortemente recomendável.

### 3 - Instalando as dependências

Para instalar as libs listadas no arquivo `requirements.txt`, execute o comando abaixo:

```
    (env)$ pip install -r requirements.txt
```
### 4 - Executando a API
Finalmente, para executar a API, basta executar o seguinte comando:

```
    (env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento, é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte, conforme abaixo:

```
    (env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

> ⚠️ O símbolo *(env)$* é apenas para ilustrar um terminal com o virtualenv ativado, não pertencendo aos comandos apresentados acima.
