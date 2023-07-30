# python-base
Repositório para estudos e práticas do curso Python Base da LINUXtips.

## Conteúdo
- [Dicas](#dicas)
- [Pyenv](#pyenv)
- [Shebang](#shebang)
- [Docstring e Metadados Dunder](#docstring-e-metadados-dunder)
- [Ambiente Virtual](#ambiente-virtual)
- [Pip](#pip)
- [Encode/Decode UTF-8](#encodedecode-utf-8)
- [Interpolação e Formatação de Textos](#interpolação-e-formatação-de-textos)
- [Tuplas](#tuplas)
- [Sets](#sets)
- [Dicionários](#dicionários)
- [Input e Output](#input-e-output)


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

**Remoção de uma versão do Python com pyenv**

`pyenv uninstall 3.11`

**Caminho de instalação do Python**

`pyenv which python3`

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

**Atualização de um pacote já instalado**
`python3 -m pip install --upgrade pip`

**Instalação de pacotes**

```shell
python3 -m pip install NomePacote          # última versão
python3 -m pip install 'NomePacote==1.0.4' # versão específica
python3 -m pip install 'NomePacote>=1.0.4' # versão mínima
```

**Exemplos comuns de opções no comando de instalação**
- `--proxy http://my_username:my_password@proxy.corp:8080`
- `--index-url http://my-package-repo.company/simple/`
- `--trusted-host my-package-repo.company:80`

**Instalação de uma lista de dependências especificadas em um arquivo**

`python3 -m pip install -r requirements.txt`

**Lista de pacotes instalados**

`python3 -m pip list`

**Informações de um pacote já instalado**

`python3 -m pip show nome-pacote`

**Remoção de pacote**

`python3 -m pip uninstall nome-pacote`

**Verificação de dependências quebradas**

`python3 -m pip check`

Para mais informações, [clique aqui](https://pip.pypa.io/en/stable/cli/).


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

O Python também oferece maneiras alternativas simples de imprimir emojis:

```python
# Usando código hexadecimal do emoji
>>> print('\U0001F34F') # \U000 + hexadecimal
🍏

# Digitando o nome do emoji
>>> print('\N{green apple}')
🍏
```

## Interpolação e Formatação de Textos
Interpolação utilizando `%`

```python
>>> mensagem = "Olá %s, você é o participante número %d e pode ganhar %.2f pontos."
>>> nome = "Renan"
>>> numero = 4
>>> pontos = 42.5
>>> print(mensagem % (nome, numero, pontos))
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

Também é possível utilizar parâmetros nomeados com `%`

```python
>>> mensagem = "Olá %(nome)s, você é o participante número %(num)d e pode ganhar %(pontos).2f pontos."
>>> print(mensagem % {
        'nome': 'Renan',
        'num': 4,
        'pontos: 42.5
    })
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

> Interpolação com `%` caiu em desuso por conta das alternativas `format` e `f strings`.

Concatenação com `format`

```python
>>> mensagem = "Olá {:s}, você é o participante número {:d} e pode ganhar {:.2f} pontos."
>>> print(mensagem.format(nome, numero, pontos))
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

Também é possível nomear as posições com `format`

```python
>>> mensagem = "Olá {nome}, você é o participante número {numero} e pode ganhar {pontos:.2f} pontos."
>>> print(mensagem.format(nome="Renan", numero=4, pontos=42.50))
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

> O uso de `format` tem diminuido com o surgimento de `f strings` no Python 3, mas ainda deve ser utilizado com a biblioteca `logging`.

Formatando textos com `format`

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

# Definindo tipo e precisão para números flutuantes
>>> "{:*^11.2f}".format(45.300041)
'***45.30***'
```

Concatenação com `f strings`

```python
>>> mensagem = f"Olá {nome}, você é o participante número {numero} e pode ganhar {pontos:.2f} pontos."
>>> print(mensagem)
Olá Renan, você é o participante número 4 e pode ganhar 42.50 pontos.
```

> Devido sua facilidade, é recomendado o uso de `f strings` para todos os demais cenários de formatação de textos.

Para mais informações, [clique aqui](https://pyformat.info)


## Tuplas
A tupla é um tipo de dados composto e imutável que pode ser declarada da seguinte maneira:

```python
>>> dados = ("Renan", 15, True, None, 57.7)
# ou sem parenteses
>>> dados = "Renan", 15, True, None, 57.7
```

Contabilizar a quantidade de um valor existente dentro da tupla

```python
>>> dados.count("Renan")
1
```

Desempacotamento de tupla

```python
>>> pontos = 1000, 1030, 7
>>> x, y, z = pontos
x # 1000
y # 1030
z # 7
```

Desempacotamento de tupla, mas descartando valores utilizando a convensão `*_`

```python
>>> x, *_ = pontos
x # 1000
_ # [1030, 7]
```

Desempacotamento de tupla, recuperando o primeiro e último valor, e descartando o restante

```python
>>> pontos = (500, 125, 607, 711, 808)
>>> head, *body, tail = pontos
head # 500
body # [125, 607, 711]
tail # 808
```

Para mais informações, [clique aqui](https://www.w3schools.com/python/python_tuples.asp)


## Sets

Conjuntos são muito úteis para resolver problemas reais do dia a dia, aqui está dois exemplos importantes:

1. Imagine em uma rede social como o Instagram, no conjunto A estão as pessoas que você segue, no conjunto B estão as que te seguem de volta, com este objeto (`set`) você consegue determinar rapidamente quem não está te seguindo de volta.

2. Performance: fazer buscas em sequência é uma operação custosa, imagina você querer encontrar o nome `Anna` no meio de uma lista com 10000 nomes. O Python teria que fazer uma iteração nessa lista e ir comparando cada item `n` da lista até encontrar, e por esse motivo, temos uma complexidade algoritmica `O(n)`.

    Os `sets` implementam uma hash table. É como se eles tivessem um índice gravado neles com uma tabela invertida, dizendo:

    ```
    "João" -> "Está na posição 0"
    "Anna" -> "Está na posição 7450"
    ```

    Portanto, quando precisarmos buscar `Anna` o Python olha primeiro essa tabela e já vai diretamente na informação que está em `7450`, como se fizessemos `users[7450]` em uma lista, e a complexidade desta operação passa a ser `O(1)`, pois agora só tem uma comparação a ser feita.

**Desvantagens dos Sets**

- Não respeitam a ordem de inserção, os elementos são ordenados automaticamente.
- Não permitem subscrição para acesso aos valores, ou seja, você não pode fazer `set[0]` para acessar o primeiro elemento. Para isso você teria que converter o set em lista e aí sim acessar o valor da posição desejada.


Criação de conjunto de números:

```python
>>> conjunto = {1, 2, 3, 4, 5}
# ou
>>> conjunto = set([1, 2, 3, 4, 5]) # recomendado
```

> Para criação de um conjunto, o `set` aceita qualquer objeto iterável: strings, listas, tuplas, etc.

Considerando as listas abaixo, veremos os diferentes cenários...

```python
>>> conjunto_a = [1, 2, 3, 4, 5]
>>> conjunto_b = [4, 5, 6, 7, 8]

# União de dois conjuntos
>>> set(conjunto_a) | set(conjunto_b)
{1, 2, 3, 4, 5, 6, 7, 8} # conjuntos descartam valores duplicados

# Intersecção de conjuntos (exibe o que existe em ambos)
>>> set(conjunto_a) & set(conjunto_b)
{4, 5} # somente valores existentes em ambos conjuntos

# Diferença entre conjuntos
>>> set(conjunto_a) - set(conjunto_b)
{1, 2, 3} # traz somente os valores existentes no conjunto_a e 
          # que não existe no conjunto_b

# Diferença simétrica (não exibe o que existe em ambos)
>>> set(conjunto_a) ^ set(conjunto_b)
{1, 2, 3, 6, 7, 8}
```

## Dicionários

Dicionário é um misto entre o `set` e `list` e são criados com `{ }` ou `dict()` usando chave e valor.

```python
# É possível criar um dicionário vazio e depois ir adicionando os elementos dentro dele:
>>> cliente = {}
# ou
>>> cliente = dict()

# Adicionar chave e valor:
>>> cliente['nome'] = 'Renan'

# Ler valor a partir de uma chave:
>>> cliente['nome']

# Alterar valor a partir de uma chave:
>>> cliente['nome'] = 'Renan Morais'

# Deletar um valor e sua chave:
>>> del cliente['nome']
```

**Buscas**

O dicionário implementa Hash Table, também conhecido como Hash Map, e portanto, as buscas em dicionário quando feitas por chave tem acesso constante O(1).

```python
>>> 'nome' in cliente
True
```

**Métodos de Lookup**

```python
>>> cliente = {
        'nome': 'Renan',
        'cidade': 'Araraquara'
    }

# Obter uma lista de chaves:
>>> cliente.keys()
dict_keys(['nome', 'cidade'])

# Obter uma lista de valores:
>>> cliente.values()
dict_keys(['Renan', 'Araraquara'])

# Obter uma lista de tuplas contendo chave e valor:
>>> cliente.items()
dict_items([('nome', 'Renan'), ('cidade', 'Araraquara')])

>>> extra = {
        'pais': 'Brasil'
    }

# Combinando 2 dicionários com desempacotamento:
>>> final = {**cliente, **extra}
{'nome': 'Renan', 'cidade': 'Araraquara', 'pais': 'Brasil'}

# Combinando 2 dicionários com update:
>>> final = cliente.update(extra)
{'nome': 'Renan', 'cidade': 'Araraquara', 'pais': 'Brasil'}
```

**Erros**

```python
# Caso uma chave não exista no dicionário, o Python exibe um erro chamado `KeyError`:
>>> print(cliente['telefone'])
KeyError 'telefone'

# Para evitar o erro podemos usar o método `get` que busca a chave e caso não exista retorna um valor padrão que inicialmente é `None`:
>>> print(cliente.get('telefone'))
'None'

>>> print(cliente.get('telefone', '191'))
'191'
```


## Input e Output

Em Python existe um módulo chamado `sys` que fornece utilidades para interagir com o sistema. Uma das utilidades por exemplo, é verificar em qual plataforma o programa está sendo executado:

```python
>>> import sys
>>> print(sys.platform)
'linux'
```

**Stdout**

No módulo `sys` também encontramos o objeto `stdout` que é o responsável por se comunicar via texto com a respectiva interface.

```python
>>> import sys
>>> sys.stdout
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
```

Este objeto é um *file descriptor* e em sistemas Linux por exemplo, tudo é baseado em descritores de arquivos. Nós podemos escrever neste descritor e o resultado será a impressão da mensagem na tela. Repare que este objeto respeita a tabela de caracteres UTF-8.

```python
>>> import sys
>>> quantidade_de_chars = sys.stdout.write('Renan')
'Renan'
>>> print(quantidade_de_chars)
5
```

Nós raramente precisaremos usar `sys.stdout` diretamente pois o Python oferece uma abstração com usabilidade melhor, que é a nossa já conhecida função `print`.

```python
>>> help(print)
print(*args, sep=' ', end='\n', file=None, flush=False)
```

Repare que `print` recebe um parâmetro `file` que por padrão é `None`, e portanto, escreve os textos no `sys.stdout`.

```python
>>> print('Hello', file=open('hello.txt', 'a'))
```

No exemplo acima o Python não irá imprimir `Hello` na tela, em vez disso vai gravar a palavra em um arquivo chamado `hello.txt` e você pode conferir com o comando `cat` no Linux.

```shell
$ cat hello.txt
Hello
```

**Stdin**

Assim como a saída padrão é o monitor ou terminal, a entrada padrão é sempre o prompt de comandos, e nós assumimos que a entrada será feita através de um teclado.

A interface para se comunicar com este dispositivo também está no módulo `sys`.

```python
>>> import sys
>>> letras = sys.stdin.read(4)
# Aqui o cursor fica esperando a digitação de 3 caracteres seguidos de enter
ABC<enter>
>>> print(letras)
'\nABC'
```

A boa notícia é que não precisamos usar da forma acima. O Python oferece uma abstração em cima desta interface que é a função `input` que serve para lermos a entrada a partir da digitação do usuário ou `stdin` do terminal.

```python
>>> nome = input('Qual o seu nome?\n')
Qual o seu nome?
# O cursor ficará esperando digitarmos algum texto seguido de enter
Renan<enter>
>>> print(nome)
'Renan'
```

A função `input` sempre irá ler as informação em formato de texto e seu argumento único é a mensagem a ser exibida para o usuário.

Uma outra utilidade para a `input` é bloquear a execução do programa até que o usuário pressione enter.

```python
>>> print('Programa fazendo alguma coisa...')
>>> input('Pressione enter quando quiser continuar...')
# Aqui o programa entra em `pausa` e só continua quando o usuário pressionar enter
```

**CLI Arguments**

Outra forma de ler informações para dentro de um script é através de argumentos de CLI. Quando usamos uma ferramenta de terminal é comum passarmos parametros para dentro do programa, como por exemplo:

```shell
python --version
python -c 'comando'
```

Repare que além do programa python passamos os parametros `--version` e o `-c 'comando'`.

Em nossos próprios scripts podemos ler essas informações através do módulo `sys`.

programa.py

```python
import sys
print(sys.argv)
```

No terminal

```shell
$ python programa.py argumento1 argumento2 --nome=Renan
['programa.py', 'argumento1', 'argumento2', '--nome=Renan']
```

A lista `sys.argv` irá coletar os argumentos passados para o programa, sendo que o nome do programa estará sempre na primeira posição, se quisermos considerar apenas os argumentos passados após o nome do programa podemos fazer um fatiamento desta lista.

programa.py

```python
import sys
print(sys.argv[1:])  # começando no elemento 1 (ignorando o 0)
```

No terminal

```shell
$ python programa.py argumento1 argumento2 --nome=Renan
['argumento1', 'argumento2', '--nome=Renan']
```

Cada item da nossa lista de argumentos será um objeto do tipo `str` portanto podemos usar qualquer operação válida com textos, por exemplo, podemos transformar os argumentos passados pelo CLI em um dicionário.

programa.py

```python
import sys

argumentos = {}

for arg in sys.argv[1:]:
    chave, valor = arg.split("=")
    argumentos[chave.lstrip('-').strip()] = valor.strip()

print(argumentos)
```

No terminal

```shell
$ python programa.py --nome=Renan --idade=26 --cidade=Araraquara
{'nome': 'Renan', 'idade': '26', 'cidade': 'Araraquara'}
```

Em nosso programa podemos usar este dicionário para tomar as decisões de fluxo do programa.

**Cuidados ao ler inputs!**

Assim como a leitura das variáveis de ambiente nos exemplos passados, tanto os `inputs` quanto as `CLI args` serão sempre lidas como texto `str`, e portanto, pode ser necessário fazer validações e transformações conforme os exemplos abaixo.

```python
# Garantir que não tenha espaços em branco no começo ou final
valor = input("Digite um valor: ").strip()

# Remover `--` em argumentos de linha de comando
valor = sys.argv[0].lstrip('-')

# Converter texto para número inteiro
valor - int(input("Digite um número: ").strip())
```
