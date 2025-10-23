from flask import Blueprint, request, jsonify
from core.professor.professor_service import ProfessorService
from core.professor.professor import Professor
from core.validador.validador import validar_dados
from auth.auth import autenticacao

professor_service = ProfessorService()

professor_controller = Blueprint('professor', __name__, url_prefix= '/professores')

@professor_controller.route('/', methods= ['GET'])
@autenticacao
def listar_professores():
    professor = professor_service.listar_professor()
    return jsonify(professor)

@professor_controller.route('/', methods= ['POST'])
@autenticacao
def adicionar_professor():
    dados = request.get_json()

     # Validação de dados
    validacao = validar_dados(dados["cpf"], dados["nome"], dados["idade"])
    if validacao != True:
        return jsonify(validacao), 400

    obj_professor = Professor(id= 0, nome= dados["nome"], idade= dados["idade"], cpf= dados["cpf"])
    professor = professor_service.adicionar_professor(obj_professor)
    return jsonify(professor), 201

@professor_controller.route('/<int:id>', methods= ['GET'])
@autenticacao
def obter_professor(id):
    professor = professor_service.obter_professor_por_id(id)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
@professor_controller.route('/<int:id>', methods= ['PUT'])
@autenticacao
def atualizar_professor():
    dados = request.get_json()

     # Validação de dados
    validacao = validar_dados(dados["cpf"], dados["nome"], dados["idade"])
    if validacao != True:
        return jsonify(validacao), 400

    obj_professor = Professor(id= dados["id"], nome= dados["nome"], idade= dados["idade"], cpf= dados["cpf"])
    professor = professor_service.atualizar_professor(obj_professor)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
@professor_controller.route('/<int:id>', methods= ['DELETE'])
@autenticacao
def remover_professor(id):
    sucesso = professor_service.remover_professor(id)
    return jsonify(sucesso)