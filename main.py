from documento import Documento
from telefonebr import TelefoneBr

cpf = "61724758004"

doc = Documento.cria_documento(cpf)
print(doc)

cnpj = "69518091000158"

docpj = Documento.cria_documento(cnpj)
print(docpj)

telef = "5519970874661"
telobj = TelefoneBr(telef)

print(telobj)