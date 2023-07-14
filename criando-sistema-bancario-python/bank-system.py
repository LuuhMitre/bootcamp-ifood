class BankSistem:
    def __init__(self):
        self.balance = 0
        self.movement = 0
        self.daily_withdrawal = 0
        self.statement = []
    
    def deposit(self, deposit_value:float):
        if deposit_value > 0:
            self.balance += deposit_value
            self.movement += 1
            self.statement.append(f'Deposito: R$ {deposit_value:.2f}')
            print(f'Depósito no valor de R$ {deposit_value:.2f} efetuado com sucesso! ')
            print(f'Seu saldo atual é de R$ {self.balance:.2f}')
            print()
        else:
            print('Valor inválido!')

    def withdrawal(self, withdrawal_value:float):
        if self.daily_withdrawal < 3:

            if self.balance < withdrawal_value: 
                print('Não foi possível realizar esta transação. Saldo insuficiente.')
            elif withdrawal_value > 500:
                print('Não foi possível realizar esta transação.')
                print('O valor máximo para o saque é de R$500,00.') 
                print()
            else:
                self.balance -= withdrawal_value
                self.movement += 1
                self.daily_withdrawal += 1
                self.statement.append(f'Saque: R$ {withdrawal_value:.2f}')
                print(f'Saque no valor de R$ {withdrawal_value:.2f} efetuado com sucesso!')
                print(f'Seu saldo atual é de R$ {self.balance:.2f}')
                print()
                
        else:
            print('Limite de saque diário atingido. Volte amanhã!')

    def show_statement(self):
        print(f'''EXTRATO BANCÁRIO 
              
Saldo Atual: R$ {self.balance:.2f} 
              
Movimentações:
              
''')


        if self.statement == []:
            print(' -- Não foram realizadas movimentações.')  
            print() 
        else:
            for item in self.statement:
                print(f'-- {item}')    

print('Bem vindo ao BANCO GRINGOTTS!')
print()
bank_sistem = BankSistem()

while True:
    option = int(input('''Selecione uma opção no MENU abaixo:

        1 - Depósito

        2 - Saque

        3 - Extrato 
                
        4 - Sair
        
    '''))

    print()
    print('###################################################')

    if option in (1, 2, 3, 4):
        if option == 1:
            value = float(input('Informe o valor do depósito: '))
            print()
            bank_sistem.deposit(value)  
            print('###################################################')
        elif option == 2:
            value = float(input('Informe o valor do saque: '))
            print()
            bank_sistem.withdrawal(value)
            print('###################################################')
        elif option == 3:
            bank_sistem.show_statement()
            print('###################################################')
        else:
            break
            
    else:
        print('Digite uma opção válida.')
        print('###################################################')



