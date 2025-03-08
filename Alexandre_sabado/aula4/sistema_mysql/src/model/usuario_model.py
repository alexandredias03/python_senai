import mysql.connector
from config import Config

class UsuarioModel:

    def __init__(self):
        # Iniciando a configuração
        self.config = Config()   

        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )

        # Faz o cursor trazer o resultado em dicionarios
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_users(self):
        query = "SELECT id, usuarioNome, email, idade FROM usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_user(self, usuarioNome, email, idade):
        # Inserir um usuario na tabela usuarios
        query = "INSERT INTO usuarios (usuarioNome, email, idade) VALUES(%s, %s, %s)"
        self.cursor.execute(query,(usuarioNome, email, idade))
        self.connection.commit()
        return self.cursor.lastrowid
        
    def get_user_by_id(self, usuario_id):
        # Buscar usuario pelo ID
        query = "SELECT id, usuarioNome, email, idade FROM usuarios WHERE id = %s"
        self.cursor.execute(query, usuario_id)
        return self.cursor.fetchone()
        
    def delete_user_by_id(self, usuario_id):
        # Deletar um usuario pelo id
        query = "DELETE FROM usuarios WHERE id = %s"                
        self.cursor.exectute(query, usuario_id)
        self.connection.commit()
        return self.cursor.rowcount
        
    def update_user_by_id(self, usuario_id, usuarioNome, email, idade):
        query = "UPDATE usuarios SET usuarioNome = %s, email = %s WHERE id = %s"
        self.cursor.execute(query, (usuarioNome, email, idade, usuario_id))
        self.connection.commit()
        return self.cursor.rowcount
        
    def close_connection(self):
        self.cursor.close()
        self.connection.close()