from flask import Blueprint, request, jsonify
from core.materia.materia_service import MateriaService
from core.materia.materia import Materia
from auth.auth import autenticacao

materia_service = MateriaService()

materia_controller = Blueprint('materia', __name__, url_prefix= '/materias')

@materia_controller.route('/', methods= ['GET'])
@autenticacao
def listar_materias():
    materias = materia_service.listar_materia()
    return jsonify(materias)

@materia_controller.route('/', methods= ['POST'])
@autenticacao
def adicionar_materia():
    dados = request.get_json()
    obj_materia = Materia(id= 0, materia= dados["materia"], sigla_curricular= dados["sigla_curricular"], descricao= dados["descricao"])
    materias = materia_service.adicionar_materia(obj_materia)
    return jsonify(materias), 201

@materia_controller.route('/<int:id>', methods= ['GET'])
@autenticacao
def obter_materia(id):
    materias = materia_service.obter_materia_por_id(id)
    if materias:
        return jsonify(materias)
    else:
        return jsonify({"erro": "Materia não encontrado"}), 404
    
@materia_controller.route('/<int:id>', methods= ['PUT'])
@autenticacao
def atualizar_materia():
    dados = request.get_json()
    obj_materia = Materia(id= dados["id"], materia= dados["materia"], sigla_curricular= dados["sigla_curricular"], descricao= dados["descricao"])
    materias = materia_service.atualizar_materia(obj_materia)
    if materias:
        return jsonify(materias)
    else:
        return jsonify({"erro": "Materia não encontrado"}), 404
    
@materia_controller.route('/<int:id>', methods= ['DELETE'])
@autenticacao
def remover_materia(id):
    sucesso = materia_service.remover_materia(id)
    return jsonify(sucesso)