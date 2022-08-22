# importa biblioteca de regex
import re

class TelefoneBr:

    # Metodo Construtor
    def __init__(self, telefone):
        # Vamos validar o telefone ao inicializar o objeto
        if self.valida_telefone(telefone):
            self._telefone = telefone
        else:
            raise ValueError("Telefone inválido!")

    # Metodo que valida o telefone
    def valida_telefone (self, telefone):
        padrao = re.compile("([1-9]{2})?\(?([1-9]{2})\)?\s?([0-9]{4,5})\s?\-?([1-9]{4})")
        retorno = padrao.match(telefone)

        if not retorno:
            return False
        else:
            return True

    # Formata numero
    def format(self):
        padrao = "([1-9]{2})?\(?([1-9]{2})\)?\s?(\d{4,5})\s?\-?(\d{4})"
        retorno = re.search(padrao, self._telefone)
        return f"+{retorno.group(1)} ({retorno.group(2)}) {retorno.group(3)}-{retorno.group(4)}"
    
    # Duck Tiping - Para o metodo print
    def __str__(self):
        return self.format()