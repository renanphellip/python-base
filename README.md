# python-base
Repositório para estudos e práticas do curso Python Base da LINUXtips

# Conteúdo
- [Dicas](#dicas)
- [Pyenv](#pyenv)
- [Sheband](#shebang)
- [Docstring e Metadados Dunder](#docstring-e-metadados-dunder)
- [Ambiente Virtual](#ambiente-virtual)
- [Pip](#pip)
- [Encode/Decode UTF-8](#encodedecode-utf-8)
- [Interpolação e Formatação de Textos](#interpolação-e-formatação-de-textos)

## Dicas
- `python3 -m site` - obtém informações sobre os caminhos de instalação do Python 3
- `dir(objeto)` - obtém uma lista de métodos especiais, atributos e métodos de funcionalidades do objeto

## Pyenv
O pyenv é uma CLI que permite instalar múltiplas versões do Python e gerenciar seu uso em escopo global da máquina ou local (em um diretório específico).

**Instalação do pyenv no MacBook**  
```shell
brew update
brew install pyenv
```

**Upgrade do pyenv**  
`brew upgrade pyenv`

**Lista de Python 3 disponíveis**  
`pyenv install -l | grep -E "^  3(\.[0-9]*){2}$"`

**Instalação do Python com pyenv**  
`pyenv install 3.11`

**Lista de versões do Python já instaladas**  
`pyenv versions`

**Escolha de versão do Python**  
- `pyenv shell <version>` - sessão do shell
- `pyenv local <version>` - diretório local
- `pyenv global <version>` - escopo global do usuário da máquina

Para mais informações, [clique aqui](https://github.com/pyenv/pyenv#readme).

## Shebang
Em ambientes Linux é muito importante definir o comentário especial Shebang dentro do arquivo Python. Nele, especificamos qual interpretador será usado para executar o programa.

```python
#!/usr/bin/env python3

print('Hello, World!')
```

A primeira linha informa o terminal que aquele programa roda com o Python 3 da `env` em execução, dessa forma, é possível omitir o interpretador e executar o script diretamente pelo seu nome.

Antes precisamos dar permissão de execução no script:
`chmod +x hello_world.py`

Agora podemos executar de 2 formas:
```shell
# Especificando o interpretador na linha de comando
python3 hello_world.py

# Usando o interpretador especificado no shebang
./hello_world.py
```

A vantagem da segunda forma é que podemos alterar a extensão de `.py` para qualquer coisa, ou podemos até remover a extensão do arquivo e executar `./hello_world` .

## Docstring e Metadados Dunder
Em todo script Python é uma boa prática incluir um comentário de multi linhas nas primeiras linhas do script explicando o objetivo do script e provendo uma documentação para o usuário.

```python
#!/usr/bin/env python3

"""Hello World Multi Linguas

Dependendo do idioma configurado no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada. Ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Renan Morais"
__license__ = "Unlicense"
```

E além do comentário de documentação, chamado `docstring`, é também comum a inclusão de variavéis de metadados que iniciam e terminam com 2 underlines `__` , a palavra que usamos para designar essas variavéis é `dunder` portanto, `dunder version` se refere a `__version__`.

## Ambiente Virtual
O ambiente virtual é um sandbox, é uma cópia de todo o ambiente Python. A recomendação é que você tenha um ambiente virtual em cada um dos seus projetos, sendo assim, cada projeto deve usar seu próprio conjunto de bibliotecas isoladamente.

**Criação de ambiente virtual**  
```shell
cd python-base
python3 -m venv .venv
```

Ao executar esse comando, irá notar que foi criada uma nova pasta chamada `.venv` e dentro dela existe a cópia de todos os arquivos do Python.

```shell
ls -a .venv
.  ..  bin  include  lib  lib64  pyvenv.cfg  share
```

Dentro da pasta `bin` podemos encontrar o `python` e também outras ferramentas como o `pip`, e a partir de agora, todos os módulos que instalarmos vão para dentro da pasta `lib`.

Mas para usar o ambiente virtual será sempre necessário efetuar sua ativação, no Linux isso é feito com o comando abaixo:

`source .venv/bin/activate`

Ao rodar o `activate` o seu prompt passa a exibir `(.venv)` que é o nome do ambiente virtual, e para se certificar, execute o comando `python3 -m site`.

Outra forma de verificar qual ambiente Python está ativado é usando o comando `which python`. O retorno deve ser algo como `.../python-base/.venv/bin/python`.

> **IMPORTANTE** sempre que abrir um terminal, antes de executar os comandos, é necessário ativar o ambiente virtual do seu projeto.

## Pip
Pip é o gerenciador de pacotes padrão do Python e com essa ferramenta é possível instalar dependências para os nossos projetos.

**Atualização do próprio pip**
`python3 -m pip install --upgrade pip`

Com o pip atualizado, vamos instalar nosso primeiro pacote, chamado IPython:
`python3 -m pip install ipython`

## Encode/Decode UTF-8
Eventualmente, durante a programação com Python, podemos ter a necessidade de salvar em um banco de dados ou transmitir textos contendo caracteres especiais ou até mesmo emojis. 

Neste caso podemos realizar o encode da string:
```python
# variável
fruit = '🍉'

# para transmitir
fruit.encode('utf-8')
b'\xf0\x9f\x8d\x89'
```

Ou o contrário para decode:
```python
# variável com encode utf-8
fruit = b'\xf0\x9f\x8d\x89'

# convertendo de bytes para string
fruit.decode('utf-8')
🍉
```

## Interpolação e Formatação de Textos
`%`
```python
>>> mensagem = "Olá %s, você é o participante número %d e pode ganhar %.2f pontos."
>>> nome = "Renan"
>>> numero = 4
>>> pontos = 42.5
>>> print(mensagem % (nome, numero, pontos))
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

Também é possível utilizar parâmetros nomeados.
```python
>>> mensagem = "Olá %(nome)s, você é o participante número %(num)d e pode ganhar %(pontos).2f pontos."
>>> print(mensagem % {
        'nome': 'Renan',
        'num': 4,
        'pontos: 42.5
    })
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

`format`
```python
>>> mensagem = "Olá {:s}, você é o participante número {:d} e pode ganhar {:.2f} pontos."
>>> print(mensagem.format(nome, numero, pontos))
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

Exemplos:
```python
# Centralizar fazendo ocupar exatamente 11 caracteres.
>>> "{:^11}".format("Renan")
'   Renan   '

# A mesma coisa porém alinhado à direita.
>>> "{:>11}".format("Renan")
'      Renan'

# Agora preenchendo os espaços com outro carectere.
>>> "{:*^11}".format("Renan")
'***Renan***'

# Definindo tipo e precisão para números
>>> "{:*^11.2f}".format(45.300041)
'***45.30***'
```
