import sys
sys.path.append("c:/Users/danie/OneDrive/Documentos/Rest APIsCom Python e Flask")

from flask_httpauth import HTTPBasicAuth
from flask import Flask, request
from flask_restful import Resource, Api
from exemplos_aulas.SQLAlchemy_exemplos.classes_tabelas import Pessoas, Atividades, Usuarios

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

@auth.verify_password
def verificacao(login, senha):
    if not (login and senha):
        return False
    
    usuario = Usuarios.query.filter_by(login=login, senha=senha).first()
    if usuario and usuario.ativo:
        return usuario
    elif usuario and not usuario.ativo:
        return False
    else:
        return False


class Pessoa(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            if pessoa:
                response = {
                    "id": pessoa.id,
                    "nome": pessoa.nome,
                    "idade": pessoa.idade
                }
            else:
                raise AttributeError("Pessoa não encontrada")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response
    
    @auth.login_required
    def put(self, nome):
        try:
            usuario_autenticado = auth.current_user()
            if usuario_autenticado:
                pessoa = Pessoas.query.filter_by(nome=nome).first()
                if pessoa:
                    dados = request.json
                    if "nome" in dados:
                        pessoa.nome = dados["nome"]
                    
                    if "idade" in dados:
                        pessoa.idade = dados["idade"]
                    
                    pessoa.save()

                    response = {
                        "id": pessoa.id,
                        "nome": pessoa.nome,
                        "idade": pessoa.idade
                    }
                else:
                    raise AttributeError("Pessoa não encontrada")
            else:
                raise AttributeError("Usuário não está autenticado.")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response

    
    @auth.login_required
    def delete(self, nome):
        try:
            usuario_autenticado = auth.current_user()
            if usuario_autenticado and usuario_autenticado.ativo:
                pessoa = Pessoas.query.filter_by(nome=nome).first()
                if pessoa:
                    mensagem = "Pessoa {} excluída com sucesso".format(pessoa.nome)
                    pessoa.delete()
                    response = {"status": "sucesso", "mensagem": mensagem}
                else:
                    raise AttributeError("Pessoa não encontrada")
            else:
                raise AttributeError("Usuário não está ativado.")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response
        
class ListaPessoas(Resource):
    def get(self):
        try:
            pessoas = Pessoas.query.all()
            response = [{"id": i.id, "nome": i.nome, "idade": i.idade} for i in pessoas]
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response
    
    @auth.login_required
    def post(self):
        try:
            usuario_autenticado = auth.current_user()
            if usuario_autenticado and usuario_autenticado.ativo:
                dados = request.json
                pessoa = Pessoas.query.filter_by(nome=dados["pessoa"]).first()
                
                if pessoa:
                    atividade = Atividades(nome=dados["nome"], pessoa=pessoa, status=dados["status"])
                    atividade.save()
                    response = {
                        "pessoa": atividade.pessoa.nome,
                        "nome": atividade.nome,
                        "id": atividade.id  
                    }
                else:
                    raise AttributeError("Pessoa não encontrada")
            else:
                raise AttributeError("Usuário não está ativado.")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response
   
class ListaAtividades(Resource):
    def get(self):
        try:
            atividades = Atividades.query.all()
            response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome, "status": i.status if i.pessoa else None} for i in atividades]
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response

    @auth.login_required
    def post(self):
        try:
            usuario_autenticado = auth.current_user()
            if usuario_autenticado and usuario_autenticado.ativo:
                dados = request.json
                pessoa = Pessoas.query.filter_by(nome=dados["pessoa"]).first()
                
                if pessoa:
                    # Usamos o método get para obter o valor do status do payload ou fornecer o padrão "Pendente"
                    atividade = Atividades(nome=dados["nome"], pessoa=pessoa, status=dados.get("status", "Pendente"))
                    atividade.save()
                    response = {
                        "pessoa": atividade.pessoa.nome,
                        "nome": atividade.nome,
                        "id": atividade.id,
                        "status": atividade.status  # Incluímos o status na resposta
                    }
                else:
                    raise AttributeError("Pessoa não encontrada")
            else:
                raise AttributeError("Usuário não está ativado.")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response

class AtividadesPorResponsavel(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            if pessoa:
                atividades = Atividades.query.filter_by(pessoa=pessoa).all()
                response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome if i.pessoa else None} for i in atividades]
            else:
                raise AttributeError("Pessoa não encontrada")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response
        
class AtividadeStatus(Resource):
    def get(self, atividade_id):
        try:
            atividade = Atividades.query.get(atividade_id)
            if atividade:
                response = {
                    "id": atividade.id,
                    "nome": atividade.nome,
                    "status": atividade.status
                }
            else:
                raise AttributeError("Atividade não encontrada")
        except AttributeError as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response

    @auth.login_required
    def put(self, atividade_id):
        try:
            usuario_autenticado = auth.current_user()
            if usuario_autenticado and usuario_autenticado.ativo:
                atividade = Atividades.query.get(atividade_id)
                if atividade:
                    dados = request.json
                    if "status" in dados:
                        atividade.status = dados["status"]
                        atividade.save()

                        response = {
                            "id": atividade.id,
                            "nome": atividade.nome,
                            "status": atividade.status
                        }
                    else:
                        raise ValueError("O campo 'status' é obrigatório")
                else:
                    raise AttributeError("Atividade não encontrada")
            else:
                raise AttributeError("Usuário não está ativado.")
        except (ValueError, AttributeError) as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        except Exception as e:
            response = {
                "status": "Error",
                "mensagem": str(e)
            }
        return response

api.add_resource(Pessoa, "/pessoa/<string:nome>/")
api.add_resource(ListaPessoas, "/pessoa/")
api.add_resource(ListaAtividades, "/atividades/")
api.add_resource(AtividadesPorResponsavel, "/atividaderesponsavel/<string:nome>/")
api.add_resource(AtividadeStatus, "/atividade/<int:atividade_id>/status")


if __name__ == "__main__":
    app.run(debug=True)