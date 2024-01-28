from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        "id": 0,
        "nome": "Rafael",
        "habilidades": ["Python", "Flask"]
    },

    {
        "id": 1,
        "nome": "Galleani",
        "habilidades": ["Python", "Django"]
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        
        except IndexError:
            response = {"status": "erro", "mensagem": "Desenvolvedor de ID {} nao existe".format(id)}
        
        except Exception:
            response = {"status": "erro", "mensagem": "Erro desconhecido! Procure o ADM da API."}

        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": "Sucesso!", "mensagem": "Resgistro excluído"}
    
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados["id"] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
        
    
api.add_resource(Desenvolvedor, "/dev/<int:id>")
api.add_resource(ListaDesenvolvedores, "/dev")
api.add_resource(Habilidades, "/habilidades")

if __name__ == ("__main__"):
    app.run(debug=True)