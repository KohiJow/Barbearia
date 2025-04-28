# Importa a instância do banco de dados que criamos (SQLAlchemy)
from banco_dados.db import db

# Importa funções para trabalhar com senhas (hash e verificação)
from werkzeug.security import generate_password_hash, check_password_hash

# Cria a classe Usuario que vai representar a tabela 'usuarios' no banco de dados
class Usuario(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'usuarios'

    # Coluna ID: chave primária única para cada usuário
    id = db.Column(db.Integer, primary_key=True)

    # Coluna nome: campo obrigatório (não pode ser nulo)
    nome = db.Column(db.String(100), nullable=False)

    # Coluna email: campo obrigatório e único (não pode repetir emails)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Coluna senha_hash: onde vamos armazenar a senha criptografada (não a senha normal)
    senha_hash = db.Column(db.String(200), nullable=False)

    # Método para definir a senha do usuário (criptografando)
    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    # Método para verificar se a senha que o usuário digitou está correta
    def checar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    # Representação em string de um usuário (útil para debug)
    def __repr__(self):
        return f'<Usuario {self.email}>'
