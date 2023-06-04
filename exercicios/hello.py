import os

__version__ = '0.1.1'

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    'pt_BR': 'Olá, Mundo!',
    'en_US': 'Hello, World!',
    'it_IT': 'Ciao, Mondo!',
    'es_SP': 'Hola, Mundo!',
    'fr_FR': 'Bonjour, Monde!'
}

print(msg.get(current_language))