from documento import CpfCnpj

cpf = "67140301000"
#cpf = "03223875077"

print(len(cpf))

CpfCnpj(cpf, "cpf")
print(CpfCnpj(cpf, "cpf"))

cnpj = "69518091000158"
cnpj = "03658060000194"

CpfCnpj(cnpj, "cnpj")
print(CpfCnpj(cnpj, "cnpj"))