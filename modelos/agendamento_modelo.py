# Importa a instância do banco de dados (SQLAlchemy)
from banco_dados.db import db

# Cria a classe Agendamento que vai representar a tabela 'agendamentos' no banco de dados
class Agendamento(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'agendamentos'

    # Coluna ID: chave primária única para cada agendamento
    id = db.Column(db.Integer, primary_key=True)

    # Coluna usuario_id: chave estrangeira, liga o agendamento a um usuário
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # Coluna servico_id: chave estrangeira, liga o agendamento a um serviço
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'), nullable=False)

    # Coluna horario_id: chave estrangeira, liga o agendamento a um horário
    horario_id = db.Column(db.Integer, db.ForeignKey('horarios.id'), nullable=False)

    # Relacionamento: facilita o acesso ao usuário diretamente pelo agendamento
    usuario = db.relationship('Usuario', backref='agendamentos')

    # Relacionamento: facilita o acesso ao serviço diretamente pelo agendamento
    servico = db.relationship('Servico', backref='agendamentos')

    # Relacionamento: facilita o acesso ao horário diretamente pelo agendamento
    horario = db.relationship('Horario', backref='agendamentos')

    # Representação do agendamento em formato de string (útil para debug)
    def __repr__(self):
        return f'<Agendamento UsuarioID: {self.usuario_id} - ServicoID: {self.servico_id} - HorarioID: {self.horario_id}>'
