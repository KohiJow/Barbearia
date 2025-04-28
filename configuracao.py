# Importa o módulo 'os' para acessar variáveis de ambiente do sistema
import os

# Classe de configuração principal do projeto
class Config:
    # Define a chave secreta usada pelo Flask para sessões e segurança
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta_padrao'

    # Configuração da URL do banco de dados (aqui usamos SQLite por simplicidade)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///barbearia.db'

    # Desativa a modificação de track de objetos para economizar memória
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações de envio de e-mail
    MAIL_SERVER = 'smtp.gmail.com'         # Servidor SMTP para envio de emails (Gmail usado como exemplo)
    MAIL_PORT = 587                        # Porta usada pelo Gmail
    MAIL_USE_TLS = True                    # Usar TLS (camada de segurança) para envio
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Email usado para enviar (pega do sistema ou define manual)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Senha do email (sempre usar variáveis de ambiente por segurança)
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@barbearia.com'
