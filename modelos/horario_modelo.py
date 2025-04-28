# Importa a instância do banco de dados (SQLAlchemy)
from banco_dados.db import db

# Cria a classe Horario que vai representar a tabela 'horarios' no banco de dados
class Horario(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'horarios'

    # Coluna ID: chave primária única para cada horário
    id = db.Column(db.Integer, primary_key=True)

    # Coluna data_hora: representa o dia e hora disponível (ex: 2024-04-29 10:00:00)
    data_hora = db.Column(db.DateTime, nullable=False)

    # Coluna disponivel: indica se o horário está livre ou já foi agendado
    disponivel = db.Column(db.Boolean, default=True)

    # Representação do horário em formato de string (útil para debug)
    def __repr__(self):
        return f'<Horario {self.data_hora} - {"Disponível" if self.disponivel else "Ocupado"}>'
