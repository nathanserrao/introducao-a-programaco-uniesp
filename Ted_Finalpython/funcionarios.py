#lista que engloba dicionários
funcionarios = [
                {'nome': 'João Alves', 'e_mail': 'joao2010@gmail.com', 'data_admissao': '02/04/2014', 'salario': 1900, 'código': 1000},
                {'nome': 'Maria da Silva', 'e_mail': 'ms1990@gmail.com', 'data_admissao': '25/08/2010', 'salario': 2500, 'código': 1001}
]
opcao_desejada = 20

while opcao_desejada != 0:
    opcao_desejada = int(input("""
    Bem vindo ao sistema de cadastrmento de funcionários, digite a opção desejada:

    1 para cadastrar um funcionário
    2 para alterar um funcionário
    3 para mostrar todos os funcionários
    4 para excluir um funcionário
    5 para adicionar um aumento de salário
    0 para sair
    """))

    print(opcao_desejada)

    #opção 1 gera código de cadastro, baseado no tamanho da lista len(funcionaários) somado por 1000 (que gera um número padronizado) e na hora de selecionar um funcionário, ele acha o index, diminuindo o numero de cadastro por 1000
    if opcao_desejada == 1:
        dados = dict()
        print("Insira as informações do funcionário novo:")
        dados["nome"] = input("Digite o nome: ")
        dados["e_mail"] = input("Digite o e-mail: ")
        dados["data_admissao"] = input("Digite o data de admissão no formato dd/mm/aaaa: ")
        dados["salario"] = int(input("Digite o salário: R$"))
        dados["código"] = (len(funcionarios) + 1000)
        funcionarios.append(dados)
        print("Funcionário cadastrado com sucesso")

    elif opcao_desejada == 2:
        cod_pessoa_escolhida = int(input("Qual o número de cadastro do funcionário que você deseja alterar?"))
        if cod_pessoa_escolhida >= 1000 <= (len(funcionarios) + 1000):
            index_desejado = cod_pessoa_escolhida - 1000
            op_desej_alterar = input("""
            Qual informação vecê deseja alterar?
            
            1 para altrar o nome
            2 para alterar o e-mail
            3 para alterar a data de admissão
            4 para alterar o salário
    
            Digite a opção desejada:
            """)

            if op_desej_alterar == "1":
                nome_novo = input("Por qual nome você deseja alterar? ")
                funcionarios[index_desejado]["nome"] = nome_novo

            if op_desej_alterar == "2":
                e_mail_novo = input("Por qual e-mail você deseja alterar? ")
                funcionarios[index_desejado]["e_mail"] = e_mail_novo

            if op_desej_alterar == "3":
                data_ad_nova = input("Por qual data de admissão você deseja alterar? ")
                funcionarios[index_desejado]["data_admissao"] = data_ad_nova

            if op_desej_alterar == "4":
                salario_novo = int(input("Por qual salário você deseja alterar? "))
                funcionarios[index_desejado]["salario"] = salario_novo
            print("Informação alterada com sucesso")
        else:
            print("Por favor, escolha uma opção válida")

    elif opcao_desejada == 3:
        print("Esta é a lista de funcionários")
        print(funcionarios)

    elif opcao_desejada == 4:
        cod_pessoa_escolhida = int(input("Qual o número de cadastro do funcionário que você deseja excluir?"))
        if cod_pessoa_escolhida >= 1000 <= len(funcionarios) + 1000:
            index_desejado = cod_pessoa_escolhida - 1000
            funcionarios.pop(index_desejado)
            print("Funcionário excluído com sucesso")
        else:
          print("Por favor, escolha uma opção válida")

    elif opcao_desejada == 5:
        cod_pessoa_escolhida = int(input("Qual o número de cadastro do funcionário de quem você deseja aumentar o salário?"))
        if cod_pessoa_escolhida >= 1000 <= len(funcionarios) + 1000:
            quantia_p_acrescentar = int(input("Digite a quantia que você deseja acrescentar"))
            index_desejado = cod_pessoa_escolhida - 1000
            funcionarios[index_desejado]["salario"] += quantia_p_acrescentar
            print("Salário adicionado com sucesso")
        else:
          print("Por favor, escolha uma opção válida")

    elif opcao_desejada == 0:
        print("Operação finalizada")

    else:
        print("Por favor escolha um código válido")