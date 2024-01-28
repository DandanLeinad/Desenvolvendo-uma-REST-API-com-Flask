# Desenvolva uma API que gerencie um cadastro de tarefas.

from flask import Flask, jsonify, request
import json

# Criando uma instância da classe
app = Flask(__name__)

# A API terá uma lista de tarefas que deverá ter os seguintes campos: id, responsável, tarefa e status

# Lista de Tarefas (exemplo inicial)
tarefas = [
    {
        "ID": 0,
        "Responsalvel": "Daniel",
        "Tarefa": "Desenvolver método GET",
        "Status": "Concluido"
    },
    {
        "ID": 1,
        "Responsalvel": "Rafael",
        "Tarefa": "Desenvolver método POST",
        "Status": "Pendente" 
    }
]

# A API deverá permitir listar todas as tarefas e também incluir novas tarefas
# O método POST deverá receber o ID e o Status e assim realizar a alteração apenas do Status e não de todo o dicionário.

# Rota para listar e adicionar tarefas
@app.route("/tarefas", methods=["POST", "GET"])
def gerenciar_tarefas():
    # GET para "listar" as tarefas
    if request.method == "GET":
        return jsonify(tarefas)
    # POST para adicionar novas tarefas
    elif request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados["ID"] = posicao
        tarefas.append(dados)
        return jsonify(tarefas)
    
# A API deverá permitir consultar uma tarefa através do ID, alterar o status de uma tarefa e também excluir uma tarefa.

# Rota para consultar, alterar status e excluir uma tarefa específica pelo ID
@app.route("/tarefas/<int:id>", methods=["GET", "PUT", "DELETE"])
def gerenciar_tarefas_especifica(id):
    # GET para consultar a tarefa e verificar se a tarefa pelo id existe
    if request.method == "GET":
        try:
            response = tarefas[id]
        
        except IndexError:
            response = {"status": "Erro", "mensagem": "Desenvolvedor de ID {} nao existe".format(id)}

        except Exception:
            response = {"status": "Erro", "mensagem": "Erro desconhecido! Procure o ADM da API."}

        return jsonify(response)
    
    elif request.method == "PUT":
        dados = json.loads(request.data)
        try:
            tarefa = tarefas[id]
            tarefa["Status"] = dados["Status"]
            return jsonify(tarefa)
        except IndexError:
            return jsonify({"status": "Erro", "mensagem": "Desenvolvedor de ID {} nao existe".format(id)})
        except Exception:
            return jsonify({"status": "Erro", "mensagem": "Erro desconhecido! Procure o ADM da API."})

    elif request.method == "DELETE":
        try:
            tarefa_removida = tarefas.pop(id)
            return jsonify({"status": "Sucesso", "mensagem": "Tarefa removida com sucesso", "tarefa_removida": tarefa_removida})
        except IndexError:
            return jsonify({"status": "Erro", "mensagem": "Desenvolvedor de ID {} nao existe".format(id)})
        except Exception:
            return jsonify({"status": "Erro", "mensagem": "Erro desconhecido! Procure o ADM da API."})

if __name__ == "__main__":
    app.run(debug=True)