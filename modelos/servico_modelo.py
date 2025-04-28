# Importa a instância do banco de dados (SQLAlchemy)
from banco_dados.db import db

# Cria a classe Servico que vai representar a tabela 'servicos' no banco de dados
class Servico(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'servicos'

    # Coluna ID: chave primária única para cada serviço
    id = db.Column(db.Integer, primary_key=True)

    # Coluna nome: nome do serviço (ex: Corte de cabelo, Barba)
    nome = db.Column(db.String(100), nullable=False)

    # Coluna descricao: descrição do serviço (ex: Corte na tesoura, degradê, etc.)
    descricao = db.Column(db.Text, nullable=True)  # Pode ser nulo (não obrigatório)

    # Coluna preco: preço do serviço
    preco = db.Column(db.Float, nullable=False)

    # Representação do serviço em formato de string (útil para debug)
    def __repr__(self):
        return f'<Servico {self.nome} - R${self.preco:.2f}>'
