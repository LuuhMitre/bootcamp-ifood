import textwrap

def menu():
    menu = """\n
    ================ MENU ================

    \n[d]\tDepositar
    \n[s]\tSacar
    \n[e]\tExtrato
    \n[nc]\tNova conta
    \n[lc]\tListar contas
    \n[nu]\tNovo Usuário
    \n[q]\tSair
    ==> """
    return input(textwrap.dedent(menu))

def deposit(balance, deposit_value, statement, /):
    if deposit_value > 0:
        balance += deposit_value
        statement += f'Depósito:\tR$ {deposit_value:.2f}\n'
        print(f'\n=== Depósito no valor de R$ {deposit_value:.2f} realizado com sucesso! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    return balance, statement

def withdraw(*, balance, withdraw_value, statement, limit, num_withdraw, withdraw_limit):
    exceeded_balance = withdraw_value > balance
    exceeded_limit = withdraw_value > limit
    exceeded_withdraw = num_withdraw >= withdraw_limit
 
    if exceeded_balance: 
        print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@\n')
    elif exceeded_limit:
        print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@\n')
    elif exceeded_withdraw:
        print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@\n')
    elif withdraw_value > 0:
        balance -= withdraw_value
        num_withdraw += 1
        statement += f'Saque:\tR$ {withdraw_value:.2f}'
        print('\n=== Saque realizado com sucesso! ===\n')
        return withdraw_value, balance

    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@\n')    

def show_statement(balance, /, *, statement):
    print('\n================ EXTRATO ================\n')
    print('Nenhuma movimentação realizada' if not statement else statement)
    print(f'\nSaldo:\t\tR$ {balance:.2f}')
    print('==========================================')

def create_user(users):
    cpf = input('Informe o CPF (apenas números): ')
    user = filter_user(cpf, users)

    if user:
        print('\n@@@ Já existe usuário com esse CPF! @@@\n')
    else:
        name = input('Informe o seu nome completo: ')
        birthday = input('Informe a data de nascimento (dd-mm-aa): ')
        address = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):')

        users.append({'nome': name, 'cpf':cpf, 'data_nascimento': birthday, 'endereco': address})
        
        print('=== Usuário criado com sucesso! ===')

def filter_user(cpf, users):
    filtered_users = [user for user in users if user['cpf']==cpf]
    return filtered_users[0] if filtered_users else None

def create_account(sort_code, account_number, users):
    cpf = input('Informe o CPF do usuário: ')
    user = filter_user(cpf, users)

    if user:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': sort_code, 'numero_conta': account_number, 'usuario': user}
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@\n')

def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Agência:\t{account['agencia']}
            C/C:\t\t{account['numero_conta']}
            Titular:\t{account['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(line))

def main():
    WITHDRAW_LIMIT = 3
    SORT_CODE = '0001'

    balance = 0
    limit = 500
    statement = ''
    num_withdraw = 0
    users = []
    accounts = []

    while True:

        option = menu()

        if option == 'd':
            deposit_value = float(input("Informe o valor do depósito: "))

            balance, statement = deposit(balance, deposit_value, statement)

        elif option == 's':
            withdraw_value = float(input('Informe o valor do saque: '))

            balance, statement = withdraw(
                balance=balance,
                withdraw_value=withdraw_value,
                statement=statement,
                limit=limit,
                num_withdraw=num_withdraw,
                withdraw_limit=WITHDRAW_LIMIT
            )

        elif option == 'e':
            show_statement(balance, statement=statement)

        elif option == 'nu':
            create_user(users)
        
        elif option == 'nc':
            account_number = len(accounts) + 1
            account = create_account(SORT_CODE, account_number, users)
            
            if account:
                accounts.append(account)

        elif option == 'lc':
            list_accounts(accounts)

        elif option == 'q':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()

