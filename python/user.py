import sqlite3 as sql

class Login:
    def __init__(self, database: str, username: str, password: str) -> None:
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None
        self.nickname = None
        self.forca = None
        self.inteligencia = None
        self.cor_de_pele = None
        self.cabelo = None
        
    
    def setar_forca(self, id: int, valor: int):
        self.conectar()
        self.cursor.execute("UPDATE users SET forca = ? WHERE id = ?", (valor, id))
        self.connection.commit()
        self.desconectar()

        return valor
    
    def setar_inteligencia(self, id: int, valor: int):
        self.conectar()
        self.cursor.execute("UPDATE users SET inteligencia = ? WHERE id = ?", (valor, id))
        self.connection.commit()
        self.desconectar()

        return valor
    
    
    def setar_cabelo(self, id: int, valor: str):
        self.conectar()
        self.cursor.execute("UPDATE users SET cabelo = ? WHERE id = ?", (valor, id))
        self.connection.commit()
        self.desconectar()

        return valor
    
    
    def setar_corpele(self, id: int, valor: str):
        self.conectar()
        self.cursor.execute("UPDATE users SET cor_pele = ? WHERE id = ?", (valor, id))
        self.connection.commit()
        self.desconectar()

        return valor


    def login(self) -> bool:
        return True if self.username == "admin" and "admin" == self.password else False


    def conectar(self) -> bool:
        if self.login():
            self.connection = sql.connect(self.database)
            self.cursor = self.connection.cursor()
            return True


    def desconectar(self) -> bool:
        self.connection.close()


    def inserir_login(self, user: str, senha: str, nickname: str) -> None:
        self.conectar()
        self.cursor.execute("INSERT INTO users (nickname, user, senha) VALUES (?, ?, ?)", (nickname, user, senha))
        self.connection.commit()
        self.desconectar()

        return (user, senha, nickname)


    # def inserir_kwdado(self, **valores: dict) -> dict:
    #     self.conectar()
    #     self.cursor.execute("INSERT INTO users (nickname, first_name, last_name, score) VALUES (?, ?, ?, ?)", (valores['nickname'], valores['first_name'], valores['last_name'], valores['score']))
    #     self.connection.commit()
    #     self.desconectar()

    #     return valores


    def atualizar_dado(self, id: int, **valores: dict) -> None:
        self.conectar()
        self.cursor.execute("UPDATE users (nickname, user, senha) WHERE id = ? VALUES (?, ?, ?)", (id, valores['nickname'], valores['user'], valores['senha']))
        self.connection.commit()
        self.desconectar()

        return valores


    def apagar_dado(self, id: int) -> None:
        self.conectar()
        backup = self.consultar_dado(id)
        self.cursor.execute("DELETE * FROM users WHERE id = ?", (id,))
        self.connection.commit()
        self.desconectar()

        return backup

    def consultar_dado(self, id: int) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchall()
        self.desconectar()

        return consulta

    def limpar_tabela(self) -> None:
        self.conectar()
        self.cursor.execute("DELETE * FROM users")
        self.connection.commit()
        self.desconectar()


    def consultar_tabela(self) -> None:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users").fetchall()
        self.desconectar()

        return consulta
    
    
    def consultar_user(self) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT user FROM users").fetchall()
        self.desconectar()
    
        return [item[0] for item in consulta]
    
    
    def consultar_nickname(self, user: str) -> list:
        self.conectar()
        dados = self.cursor.execute("SELECT nickname FROM users").fetchall()
        
        for dado in dados:
            if dado == user:
                return dado
            else:
                return "Error"
        
        self.desconectar()
    
    
    
    def consultar_senha(self, user: str) -> None:
        self.conectar()
        
        dados = self.cursor.execute("SELECT * FROM users").fetchall()
        
        for dado in dados:
            if dado[2] == user:
                consulta = dado[3]
        
        # consulta = self.cursor.execute("SELECT senha FROM users WHERE id = ?", (id,)).fetchall()
        self.desconectar()

        return consulta
    
    
    def consultar_id(self, user: str) -> None:
        self.conectar()
        
        dados = self.cursor.execute("SELECT * FROM users").fetchall()
        
        for dado in dados:
            if dado[2] == user:
                consulta = dado[0]
        
        self.desconectar()

        return consulta


if __name__ == "__main__":
    pass