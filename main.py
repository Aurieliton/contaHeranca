class Conta:
    def __init__(self, n_conta, cliente, saldo):
        self.n_conta = n_conta
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self,valor):
        if valor >0:
            self.saldo += valor
            print('Deposito Realizado:')
            print(f'Saldo Atual: {self.saldo}')


    def exibirDados(self):
        print(f"Número da conta: {self.n_conta}")
        print(f"Nome: {self.cliente}")
        print(f"Saldo: {self.saldo}")


class ContaCorrente(Conta):
    def __init__(self, n_conta, cliente, saldo, chequeEspecial):
        super().__init__(n_conta, cliente, saldo)
        self.chequeEspecial = chequeEspecial


    def exibirDados(self):
        super().exibirDados()
        print(f'Cheque Especial: {self.chequeEspecial}')


class ContaPoupanca(Conta):
    def __init__(self,n_conta, cliente, saldo,rendimento):
       super().__init__(n_conta, cliente, saldo)
       self.rendimento = rendimento


    def exibirDados(self):
        super().exibirDados()
        print(f'Rendimento: {self.rendimento}')



conta = Conta(1, "Alberto", 1000)
conta.exibirDados()
print('')
print('')

cc = ContaCorrente(1, "Alberto", 1000,300)
cc.exibirDados()
print('')
print('')


cp = ContaPoupanca(1, "Alberto", 1000,0.5)
cp.exibirDados()
print('')
print('')