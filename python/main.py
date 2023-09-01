from user import Login as system

login_system = system("database.db", "admin", "admin")

fechar_jogo = "nao"

user = None
senha = None
nickname = None
id = None

while user == None or senha == None or nickname == None:
    while id == None:
        print("\nFaça login ou crie sua conta\n")

        user = input("Digite seu usuário: ")

        if (user in login_system.consultar_user()):
            login = input("Deseja fazer login? (Sim/Não) ")

            if (login.lower() == "sim"):
                senha = input("Digite sua senha: ")

                if (login_system.consultar_senha(user) == senha):
                    print("Logado com sucesso, bem-vindo.")

                    id = login_system.consultar_id(user)
                    nickname = login_system.consultar_nickname(user)
                else:
                    print("Senha errada.")
                    print("Crie um novo usuário ou envie a senha correta.")
            else:
                print("Ok, crie uma nova conta. Se a conta com este nome de usuário não for sua crie com outro nome.")
        else:
            senha = input("Digite sua senha: ")
            nickname = input("Digite um nickname: ")

            if (nickname in login_system.consultar_nickname()):
                print("Este nickname ja existe, utilize outro nickname.")
            else:
                new_conta = login_system.inserir_login(user, senha, nickname)

                print(f"Sua conta foi criada com os seguintes dados: {new_conta}")

                id = login_system.consultar_id(user)

# Inteligencia: 1 a 10
# Força: 1 a 10
# Cabelo: Liso, Cacheado, Ondulado
# Cor de Pele: Branca, Parda, Preto

inteligencia = int(input("Qual a inteligência do seu personagem? (1 a 10) "))
forca = int(input("Qual a força do seu personagem? (1 a 10) "))
cabelo = str(input("Qual seu tipo de cabelo? (Liso, Cacheado, Ondulado) "))
corpele = str(input("Qual a cor de pele? (Branca, Parda, Preto) "))

login_system.setar_cabelo(id, cabelo)
login_system.setar_corpele(id, corpele)
login_system.setar_forca(id, forca)
login_system.setar_corpele(id, corpele)

dados = login_system.consultar_tabela()

for dado in dados:
    print(dado[0])
    print(dado[1])
    print(dado[2])
    print(dado[3])
    print(dado[4])
    print(dado[5])
    print(dado[6])
    print(dado[7])
    