import requests
import json
import re

key_nomes = ['id', 'placa', 'marca', 'modelo', 'ano', 'automatico']
key_widths = [10, 10, 15, 15, 10, 20]
h_close = {'Connection': 'Close'}
h_content = {'Content-Type': 'application/json'}

def check_server(registro_id=None):
    url = 'http://localhost:3000/'
    if registro_id is not None:
        url += f"/{registro_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def print_menu():
    print("+-----------------------------------+")
    print("| Database - Registro de Veículos   |")
    print("+-----------------------------------+")
    print("1. Listar todos veículos")
    print("2. Busca de veículo por Placa")
    print("3. Adicionar um novo veículo")
    print("4. Deletar um registro")
    print("5. Atualizar um registro")
    print("6. Deletar todos os registros")
    print("0. Sair")

def read_user_opcao():
    opcao = input("Digite a opção: ")
    while opcao not in ['0', '1', '2', '3', '4', '5', '6']:
        opcao = input("Opção inválida! Tente novamente, conforme tabela acima: ")
    return opcao

def print_header():
    print("+", end='')
    for i in range(len(key_nomes)):
        print("-" * key_widths[i] + "+", end='')
    print()

    for i in range(len(key_nomes)):
        print(f"| {key_nomes[i]:<{key_widths[i]}}", end='')
    print("|")

    print("+", end='')
    for i in range(len(key_nomes)):
        print("-" * key_widths[i] + "+", end='')
    print()

def print_registro(registro):
    for i in range(len(key_nomes)):
        if key_nomes[i].lower() in registro:
            print(f"| {registro[key_nomes[i].lower()]:<{key_widths[i]}}", end='')
        else:
            print(f"| {'':<{key_widths[i]}}", end='')
    print("|")

def listar_registros():
    response = requests.get('http://localhost:3000/registros')
    if response.status_code == 200:
        registros = response.json()
        print_header()
        for registro in registros:
            print_registro(registro)
    else:
        print("Falha ao recuperar os registros no servidor")

def nome_is_valid(nome):
    if nome and all(c.isalnum() or c.isspace() for c in nome):
        return True
    return False

def enter_id():
    response = requests.get('http://localhost:3000/registros', headers=h_content)
    if response.status_code == 200:
        registros = response.json()
        if not registros:
            return 1
        last_id = registros[-1]['id']
        return last_id + 1
    else:
        print("Erro ao obter registros: ", response.status_code)
        return None


def enter_placa():
    registro_placa = input("Placa do veículo (XXX-0000): ").upper()
    while not re.match(r"^[A-Z]{3}-\d{4}$", registro_placa):
        print("Placa inválida. Por favor, digite no formato XXX-0000.")
        registro_placa = input("Placa do veículo (XXX-0000): ").upper()
    return registro_placa

def placa_exists(placa):
    response = requests.get(f'http://localhost:3000/registros?placa={placa}', headers=h_content)
    if response.status_code == 200:
        data = json.loads(response.content)
        return len(data) > 0
    else:
        return False

def enter_ano():
    year = input("Ano de producao do registro: ")
    if not year:
        return None
    while not (year.isdigit() and 1900 <= int(year) <= 2023):
        print("Ano inválido.")
        year = input("Digite um ano valido (1900-2023): ")
    return int(year)

def enter_nome(what):
    nome = input(f"registro {what} : ")
    if not nome:
        return None
    while not nome_is_valid(nome):
        print(f"Invalido {what} nome.")
        nome = input(f"registro {what}: ")
    return nome

def enter_automatico():
    automatico = input("O registro é automatico (S/N): ")
    if not automatico:
        return None
    while automatico.lower() not in ['s', 'n']:
        print("Resposta inválida. Apenas 'S' or 'N'.")
        automatico = input("Is the registro automatico (S/N): ")
    return 'True' if automatico.lower() == 's' else 'False'

def add_registro():
    registro = {}
    registro['id'] = enter_id()
    registro['placa'] = enter_placa()
    if placa_exists(registro['placa']):
        print("Erro: placa já em uso")
        return      
    registro['marca'] = enter_nome('marca')
    registro['modelo'] = enter_nome('modelo')
    registro['ano'] = enter_ano()
    registro['automatico'] = enter_automatico()
    if not all(registro.values()):
        print("Falha ao adicionar o registro")
        return
    response = requests.post('http://localhost:3000/registros', headers=h_content, data=json.dumps(registro))
    if response.status_code == 201:
        print("Registro adicionado com sucesso")
    else:
        print("Falha ao adicionar o registro")

def delete_registro():
    placa = enter_placa()
    response = requests.get(f'http://localhost:3000/registros?placa={placa}', headers=h_content)
    if response.status_code == 200 and response.json():
        registrados = response.json()
        print_header()
        for registro in registrados:
            print_registro(registro)
        confirmacao = input("Para confirmar a exclusão do registro, digite excluir: ")
        if confirmacao == 'excluir':
            registro = response.json()[0]
            response = requests.delete(f'http://localhost:3000/registros/{registro["id"]}', headers=h_content)
            if response.status_code == 200:
             print(f"Registro com placa {placa} excluído com sucesso")
            else:
                print("Falha ao excluir o registro")
    else:
        print(f"Não há registros com a placa {placa}")

def delete_all_registro():
    response = requests.get(f'http://localhost:3000/registros', headers=h_content)
    if response.status_code == 404:
        print("Não existe registro do registro")
        return
   
    registros = response.json()
    print_header()
    for registro in registros:
        print_registro(registro)
   
    confirmacao = input("Para confirmar a exclusão de todos os registros, digite excluir: ")
    if confirmacao == 'excluir':
        registros = response.json()
        for registro in registros:
            response = requests.delete(f'http://localhost:3000/registros/{registro["id"]}', headers=h_content)
            if response.status_code == 200:
                print(f"registro {registro['id']} deleted successfully")
            else:
                print(f"Failed to delete registro {registro['id']}")
    else:
        print('Você não digitou a palavra excluir. Não foi possível excluir os registros.')

def update_registro():
    placa = enter_placa()
    response = requests.get(f'http://localhost:3000/registros?placa={placa}', headers=h_content)
    if response.status_code == 200 and response.json():
        registrados = response.json()
        print_header()
        for registro in registrados:
            print_registro(registro)
            print("Atualize os campos ou deixe vazio para manter os valores antigos:")
        
        registro = response.json()[0]
        new_registro = {}
        new_registro['placa'] = registro['placa']
        new_registro['marca'] = enter_nome('marca') or registro['marca']
        new_registro['modelo'] = enter_nome('modelo') or registro['modelo']
        new_registro['ano'] = enter_ano() or registro['ano']
        new_registro['automatico'] = enter_automatico() or registro['automatico']
        
        if not all(new_registro.values()):
            print("Falha ao atualizar o registro")
            return
    
    response = requests.put(f'http://localhost:3000/registros/{registro["id"]}', headers=h_content, data=json.dumps(new_registro))
    if response.status_code == 200:
        print("registro atualizado com sucesso")
    else:
        print("Falha ao atualizar o registro")

def busca_placa():
    placa = input("Digite a placa do veículo (XXX-0000): ").upper()
    while not re.match(r"^[A-Z]{3}-\d{4}$", placa):
        print("Placa inválida. Por favor, digite no formato XXX-0000.")
        placa = input("Digite a placa do veículo (XXX-0000): ").upper()
    response = requests.get(f'http://localhost:3000/registros?placa={placa}', headers=h_content)
    if response.status_code == 200 and response.json():
        registro = response.json()[0]
        print_header()
        print_registro(registro)
    else:
        print(f"Não foi encontrado um veículo com a placa {placa}")


while True:
    if not check_server():
        print("Servidor sem resposta!")
        exit(1)
    print_menu()
    opcao = read_user_opcao()
    if opcao == '0':
        print("Encerrado!")
        exit(0)
    elif opcao == '1':
        listar_registros()
    elif opcao == '2':
        busca_placa()
    elif opcao == '3':
        add_registro()
    elif opcao == '4':
        delete_registro()
    elif opcao == '5':
        update_registro()
    elif opcao == '6':
        delete_all_registro()
