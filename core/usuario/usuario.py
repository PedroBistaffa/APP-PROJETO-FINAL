class Usuario:
    def __init__(self, id= None, user= "", senha= "", ativo= False):
        self.__id = id
        self.__user = user
        self.__senha = senha
        self.__ativo = ativo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id 

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, novo_user):
        self.__user = novo_user

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha_idade):
        self.__senha = senha_idade
    
    @property
    def ativo(self):
        return self.__ativo