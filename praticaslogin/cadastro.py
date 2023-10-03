import PySimpleGUI as sg

usuario_logado = ''

def tela_inicial():
    layout = [
        [sg.Button('Fazer Cadastro')],
        [sg.Button('Entrar')],
        [sg.Button('Sair')],
    ]

    window = sg.Window("Tela Inicial", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Fazer Cadastro':
            window.close()
            tela_cadastro()
        elif event == 'Entrar':
            window.close()
            tela_entrar()
        elif event == 'Sair':
            window.close()

def tela_cadastro():
    cadastro = [
        [sg.Text('Nome')],
        [sg.Input(key='nome')],
        [sg.Text('Usuario')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('Criar Cadastro')],
    ]

    window = sg.Window("Cadastro", cadastro)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event  == "Criar Cadastro":
            nome = values['nome'].strip()
            usuario = values['usuario'].strip()
            senha = values['senha'].strip()

            if not nome or not usuario or not senha:
                sg.popup_error('Todos os campos são Obrigatório. Favor Preencher')
            else:

            # Salvar o cadastro em um arquivo de texto
                salvar_cadastro(values['nome'], values['usuario'], values ['senha'])
                window.close()
                tela_cadastro_concluido()
            #Cadastro não concluído
      
def salvar_cadastro(nome, usuario, senha):
     # Abrir o arquivo em modo de escrita ('w') e adicionar o cadastro
     with open('cadastro.txt', 'a') as arquivo:
         arquivo.write(f'{nome},{usuario},{senha}\n')

def tela_cadastro_concluido():
    concluido = [
        [sg.Text('Parabéns, seu cadastro foi concluído!')],
        [sg.Button('Voltar para o Menu')],
    ]

    window = sg.Window("Cadastro", concluido)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Voltar para o Menu":
            window.close()
            tela_inicial()

def tela_entrar():
    global usuario_logado
    login = [
        [sg.Text('Login')],
        [sg.Input(key='login')],
        [sg.Text('Senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Button('Entrar')],
    ]

    window = sg.Window('Login', login)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Entrar':
            global usuario_logado
            usuario = values['login']
            senha = values ['senha']
            #print(f"Dados de Login: Usuário: {usuario}, Senha: {senha}")

        if verificar_dados(usuario, senha):
            usuario_logado = usuario
            window.close()
            tela_entrar_concluido()
            return
        else:
                sg.popup_error('Credenciais incorretas. Tente novamente.')

def verificar_dados(usuario, senha):
    with open('cadastro.txt', 'r') as arquivo:
        linhas =  arquivo.readlines()

    for linha in linhas:
        credencias = linha.strip().split(',')
        if len(credencias) == 3:
            nome, usuario_arquivo, senha_arquivo = credencias
            #print(f"Verificando: Usuário: {usuario_arquivo}, Senha: {senha_arquivo}")
            #print(f"Credenciais do Arquivo: Usuário: {usuario_arquivo}, Senha: {senha_arquivo}")
            if usuario == usuario_arquivo and senha == senha_arquivo:
                #print("Credenciais corretas!")
                return True
            
    return False

            

def tela_entrar_concluido():
    login_sucesso = [
        [sg.Text(f'Login Realizado com Sucesso! Seja bem-vindo {usuario_logado} !')],
        [sg.Button('Logout')]
    ]

    window = sg.Window('Login Concluído', login_sucesso)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Logout':
            
            window.close()
            tela_inicial()
            


# Iniciar com a tela inicial
tela_inicial()
