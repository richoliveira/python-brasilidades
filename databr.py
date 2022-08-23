# importa biblioteca datetime - trabalhar com data e hora
from datetime import datetime, timedelta

# Cria nossa classe para tabalahr com Datas
class DataBr:

    # Metodo Contrutor
    def __init__(self):
        self._momto_cadto = datetime.today()

    # Metodo retorno mes do cadastro
    @property
    def mes_cadastro(self):
        # Dicionario meses do Ano para de/para
        meses_ano = {
            1:"Janeiro", 2:"Fevereiro", 3:"Março",
            4:"Abril", 5:"Maio", 6:"Junho",
            7:"Julho", 8:"Agosto", 9:"Setembro",
            10:"Outubro", 11:"Novembro", 12:"Dezembro"
        }
        mes_cadto = self._momto_cadto.month
        return meses_ano[mes_cadto]

    # Metodo Retorna dia da semana
    @property
    def dia_semana(self):
        # Dicionario dia das semana para realizar o de/para
        # 0 = segunda-feira | 6 = Domingo
        dia_semana = {
            0:"Segunda", 1:"Terça", 2:"Quarta", 3:"Quinta",
            4:"Sexta", 5:"Sabado", 6:"Domingo"
        }
        id_dia = self._momto_cadto.weekday()
        return dia_semana[id_dia]

    # Metodo formata data
    def format(self):
        data_formatada = self._momto_cadto.strftime("%d/%m/%Y %H :%M:%S")
        return data_formatada
    
    # Duck Typing para string
    def __str__(self):
        return self.format()

    # Metodo que retorna o tempo de cadastro
    def tempo_cadastro(self):
        tp_cadtro = (datetime.today() + timedelta(days=30, hours=2, minutes=15, seconds=30)) - self._momto_cadto
        return tp_cadtro