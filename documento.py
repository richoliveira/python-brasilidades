# Importa a classe CPF do pacote de validadador de documentos
from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self._tipo_documento = tipo_documento.lower()
        if self._tipo_documento == "cpf":
            if self.cpf_valido(str(documento)):
                self._cpf = documento
            else:
                raise ValueError("CPF Inválido!")
        elif self._tipo_documento == "cnpj":
            if self.cnpj_valido(str(documento)):
                self._cnpj = documento
            else:
                raise ValueError("CNPJ Inválido!")
        else:
            raise ValueError("Tipo de documento inválido!")

    # Valida o CPF
    def cpf_valido(self, documento):
        if len(documento) == 11:
            validador_cpf = CPF()
            return validador_cpf.validate(documento)
        else:
            raise ValueError("Quantidade de números Inválido!")

    def cnpj_valido(self, documento):
        if len(documento) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(documento)
        else:
            raise ValueError("Quantidade de números inválidos!")

    # Fomata CpfCnpj - utiliza o slice/fatiamento de strings
    def doc_formatado(self):
        if self._tipo_documento == "cpf":
            cpf_mask = CPF()
            return cpf_mask.mask(self._cpf)
        elif self._tipo_documento == "cnpj":
            cnpj_mask = CNPJ()
            return cnpj_mask.mask(self._cnpj)

    # Duck Typing - string
    def __str__(self):
        return self.doc_formatado()