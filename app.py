from flask import Flask
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import usuario_controller
from core.professor.professor_controller import professor_controller

app = Flask(__name__)

# Registro das controllers
app.register_blueprint(aluno_controller)
app.register_blueprint(usuario_controller)
app.register_blueprint(professor_controller)

if __name__ == "__main__":
    app.run(debug=True)