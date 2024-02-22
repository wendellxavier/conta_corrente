from datetime import datetime
import pytz
class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = 0
        self.limite = None
        self. transacoes = []

    def consultar_saldo(self):
        print(f'seu saldo atual é de: R${self.saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        self.saldo =+ valor
        self.transacoes.append((valor, (f'saldo{self.saldo}'), ContaCorrente._data_hora()))
    
    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print(f'você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, (f'saldo{self.saldo}'), ContaCorrente._data_hora()))
    
    def consultar_limite_chequeespecial(self):
        print(f'seu limite de cheque especial é de: R${self.limite:,.2f}')

    def consultar_historico_transacoes(self):
        print('Historico de transações')
        for transacao in self.transacoes:
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))
        


#programa:
conta_usuario = ContaCorrente('wendell', '444.555.667-23', 1234, 2048)
conta_usuario.consultar_saldo()
#depositar
conta_usuario.depositar_dinheiro(2000)
conta_usuario.consultar_saldo()
#sacar
conta_usuario.sacar_dinheiro(300)
print('saldo final')
conta_usuario.consultar_saldo()

print('-'* 60)
conta_usuario.consultar_historico_transacoes()

print('-'* 60)
conta_usuario2 = ContaCorrente('felipe', '667.555.444-25', 1239, 3058)
conta_usuario.transferir(100, conta_usuario2)

conta_usuario.consultar_saldo()
conta_usuario2.consultar_saldo()
print('-'* 60)
conta_usuario.consultar_historico_transacoes()
print('-'* 60)
conta_usuario2.consultar_historico_transacoes()