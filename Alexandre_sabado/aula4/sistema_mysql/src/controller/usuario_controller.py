from ..model.usuario_model import UsuarioModel

def listar_usuarios():
    modelDois = UsuarioModel()
    usuarios = modelDois.get_all_users()
    modelDois.close_connection()
    return usuarios

def cadastrar_usuario(usuarioNome, email, idade):
    modelDois = UsuarioModel()
    novo_id_usuario = modelDois.insert_user(usuarioNome, email, idade)
    modelDois.close_connection()
    return novo_id_usuario

def atualizar_usuario(usuario_id, usuarioNome, email, idade):
    modelDois = UsuarioModel()
    linhasAftUsuarios = modelDois.update_user_by_id(usuario_id, usuarioNome, email, idade)
    modelDois.close_connection()
    return linhasAftUsuarios

def remover_usuario(usuario_id):
    modelDois = UsuarioModel()
    linhasAftUsuarios = modelDois.delete_user_by_id(usuario_id)
    modelDois.close_connection()
    return linhasAftUsuarios

def obter_usuario(usuario_id):
    modelDois = UsuarioModel()
    usuarios = modelDois.get_user_by_id(usuario_id)
    modelDois.close_connection()
    return usuarios