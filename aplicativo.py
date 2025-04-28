# Importa a biblioteca Flask para criar o aplicativo web
from flask import Flask

# Importa a configuração padrão (chaves secretas, banco de dados, etc.)
from configuracao import Config

# Importa a instância do banco de dados
from banco_dados.db import db

# Importa o JWT para autenticação de usuários
from flask_jwt_extended import JWTManager

# Importa o Mail para envio de emails
from flask_mail import Mail

# Importa as rotas (conjuntos de caminhos de API separados)
from rotas.usuario_rota import usuario_bp
from rotas.servico_rota import servico_bp
from rotas.agendamento_rota import agendamento_bp
from rotas.imagem_rota import imagem_bp
from rotas.confirmacao_agendamento_rota import confirmacao_agendamento_bp

# Cria a instância principal do aplicativo Flask
app = Flask(__name__)

# Aplica as configurações do projeto no app
app.config.from_object(Config)

# Inicializa o banco de dados dentro do app Flask
db.init_app(app)

# Inicializa o JWT (para gerar tokens de login)
jwt = JWTManager(app)

# Inicializa o Mail (para mandar emails de confirmação)
mail = Mail(app)

# Registro dos blueprints (módulos de rotas separados) com prefixo de URL
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(servico_bp, url_prefix='/servico')
app.register_blueprint(agendamento_bp, url_prefix='/agendamento')
app.register_blueprint(imagem_bp, url_prefix='/imagem')
app.register_blueprint(confirmacao_agendamento_bp, url_prefix='/confirmacao')

# Roda o aplicativo Flask se o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # 'debug=True' ajuda a ver erros enquanto desenvolve
