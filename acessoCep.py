# importa bibliotecas
import requests

class BuscaEndereco:

    # Metodo construtor
    def __init__(self, nr_cep):
        if self.validaCep(str(nr_cep)):
            self._cep = nr_cep
        else:
            raise ValueError("Cep Inválido!")
        
    # Metodo valida Cep
    def validaCep(self, nr_cep):
        if len(nr_cep) == 8:
            return True
        else:
            return False
    
    # Metodo para formatar cep
    def format(self):
        return f"{self._cep[:5]}-{self._cep[5:]}"

    # Metodo Duck Typing - Representacao de str
    def __str__(self):
        return self.format()

    # Metodo que retorna a requsicao da API
    def acesso_via_cep(self):
        url = f"https://viacep.com.br/ws/{self._cep}/json/"
        # Faz a requisicao
        req = requests.get(url)
        dados = req.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
    
