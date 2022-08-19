# Importa a classe CPF do pacote de validadador de documentos
from validate_docbr import CPF, CNPJ


# Classe Refaturadas
class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade invalida de numeros!")


#######################################
# Classe para validar e formatar CPF ##
#######################################
class DocCpf:

    # Metodo construtor
    def __init__(self, documento):
        if self.valida(documento):
            self._cpf = documento
        else:
            raise ValueError("CPF Inválido!")

    # Metodo Valida o Cpf
    def valida(self, documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    # Formata o Cpf - Mascara
    def format(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self._cpf)

    # Duck Tiping - Metodo devolve a string formatada
    def __str__(self):
        return self.format()


#######################################
# Classe para validar e formatar CNPJ #
#######################################
class DocCnpj:

    # Metodo construtor
    def __init__(self, documento):
        if self.valida(documento):
            self._cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!")

    # Metodo Valida o CNPJ
    def valida(self, documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    # Formata o CNPJ - Mascara
    def format(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self._cnpj)

    # Duck Tiping - Metodo devolve a string formatada
    def __str__(self):
        return self.format()
