# Importa o modelo de Usuário para poder manipulá-lo
from modelos.usuario_modelo import Usuario

# Importa o banco de dados para salvar as alterações
from banco_dados.db import db

# Função para criar um novo usuário
def criar_usuario(nome, email, telefone):
    # Cria um novo objeto do tipo Usuario com os dados recebidos
    novo_usuario = Usuario(nome=nome, email=email, telefone=telefone)
    
    # Adiciona o novo usuário à sessão do banco
    db.session.add(novo_usuario)
    
    # Confirma as alterações (salva no banco)
    db.session.commit()
    
    # Retorna o novo usuário criado
    return novo_usuario

# Função para listar todos os usuários cadastrados
def listar_usuarios():
    # Busca todos os usuários no banco de dados
    return Usuario.query.all()

# Função para buscar um usuário específico pelo ID
def buscar_usuario(id):
    # Busca o usuário pelo ID fornecido
    return Usuario.query.get(id)

# Função para atualizar os dados de um usuário existente
def atualizar_usuario(id, nome=None, email=None, telefone=None):
    # Busca o usuário que será atualizado
    usuario = Usuario.query.get(id)
    
    # Se o usuário for encontrado
    if usuario:
        # Atualiza os campos somente se valores novos forem passados
        if nome:
            usuario.nome = nome
        if email:
            usuario.email = email
        if telefone:
            usuario.telefone = telefone
        
        # Salva as alterações no banco
        db.session.commit()
    
    # Retorna o usuário atualizado (ou None se não encontrado)
    return usuario

# Função para deletar um usuário pelo ID
def deletar_usuario(id):
    # Busca o usuário que será deletado
    usuario = Usuario.query.get(id)
    
    # Se o usuário existir, remove do banco
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    
    # Retorna o usuário deletado (ou None se não encontrado)
    return usuario
