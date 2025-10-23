class Materia:
    def __init__(self, id= 0, materia= "", sigla_curricular= "", descricao= ""):
        self.__id = id
        self.__materia = materia
        self.__sigla_curricular = sigla_curricular
        self.__descricao = descricao

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id 

    @property
    def materia(self):
        return self.__materia
    @materia.setter
    def materia(self, nova_materia):
        self.__materia = nova_materia

    @property
    def sigla_curricular(self):
        return self.__sigla_curricular
    @sigla_curricular.setter
    def sigla_curricular(self, nova_sigla_curricular):
        self.__sigla_curricular = nova_sigla_curricular

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao
