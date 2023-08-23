class SistemaLogin:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, username, password):
        if username in self.usuarios:
            print("Nome de usuário já existe. Escolha outro nome.")
        else:
            self.usuarios[username] = password
            print("Registro bem-sucedido. Faça o login para acessar sua conta.")

    def fazer_login(self, username, password):
        if username in self.usuarios and self.usuarios[username] == password:
            print("Login bem-sucedido. Bem-vindo,", username)
            return True
        else:
            print("Credenciais inválidas. Verifique seu nome de usuário e senha.")
            return False

class Usuario:
    def __init__(self, username):
        self.username = username
        self.personalizacao = {}

    def personalizar(self, atributo, valor):
        self.personalizacao[atributo] = valor
        
sistema = SistemaLogin()
sistema.registrar_usuario("usuario123", "senha123")

if sistema.fazer_login("usuario123", "senha123"):
    usuario = Usuario("usuario123")
    usuario.personalizar("forca", 8)
    usuario.personalizar("inteligencia", 7)