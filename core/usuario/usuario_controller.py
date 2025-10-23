from flask import Blueprint, request, jsonify
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario
from auth.auth import autenticacao

usuario_service = UsuarioService()

usuario_controller = Blueprint('usuario', __name__, url_prefix= '/usuarios')

@usuario_controller.route('/', methods= ['GET'])
@autenticacao
def listar_usuario():
    usuarios = usuario_service.listar_usuario()
    return jsonify(usuarios)

@usuario_controller.route('/', methods= ['POST'])
@autenticacao
def adicionar_usuario():
    dados = request.get_json()
    obj_usuario = Usuario(id= None, user= dados["usuario"], senha= dados["senha"], ativo= dados["ativo"])
    usuario = usuario_service.adicionar_usuario(obj_usuario)
    return jsonify(usuario), 201

@usuario_controller.route('/<int:id>', methods= ['GET'])
@autenticacao
def obter_usuario(id):
    usuario = usuario_service.obter_usuario_por_id(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"erro": "Usuário ou senha incorretos"}), 404
    
@usuario_controller.route('/<int:id>', methods= ['PUT'])
@autenticacao
def atualizar_usuario():
    dados = request.get_json()
    obj_usuario = Usuario(id= dados["id"], user= dados["usuario"], senha= dados["senha"], ativo= dados["ativo"])
    usuario = usuario_service.atualizar_usuario(obj_usuario)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"erro": "Usuário ou senha incorretos"}), 404
    
@usuario_controller.route('/<int:id>', methods= ['DELETE'])
@autenticacao
def remover_usuario(id):
    sucesso = usuario_service.remover_usuario(id)
    return jsonify(sucesso)