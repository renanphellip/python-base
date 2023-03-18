# python-base
Repositório para estudos e práticas do curso Python Base da LINUXtips

## pyenv
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
`pyenv install 3.11.2`

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