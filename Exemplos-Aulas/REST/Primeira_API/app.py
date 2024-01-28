from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/<int:id>")
def pessoa(id):
    return jsonify(
        {
            "id": id,
            "nome": "Daniel",
            "Idade": 19
        }
    )

# @app.route("/soma/<int:valor1>/<int:valor2>/")
# def soma(valor1, valor2):
#     return jsonify({"Soma": valor1 + valor2})

@app.route("/soma", methods=["POST", "GET"])
def soma():
    if request.method == "POST":
        dados = json.loads(request.data)
        total = sum(dados["Valores"])
    
    elif request.method == "GET":
        total = 10 + 10
    
    return jsonify({"Soma": total})

if __name__ == "__main__":
    app.run(debug=True)