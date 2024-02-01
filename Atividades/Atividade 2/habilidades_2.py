from flask_restful import Resource
from flask import request
import json

# Lista de habilidades inicial
lista_habilidades = ["Python", "Java", "Flask", "PHP"]

class Habilidades(Resource):
    # Método GET
    def get(self):
        # Retorna a lista de habilidades
        return lista_habilidades
    
    # Método POST
    def post(self):
        try:
            # Converte os dados da requisição para JSON
            dados = json.loads(request.data)
            
            # Verifica se os dados são uma lista de strings
            if isinstance(dados, list) and all(isinstance(habilidade, str) for habilidade in dados):
                # Adiciona novas habilidades à lista, se não estiverem presentes
                for habilidade in dados:
                    if habilidade not in lista_habilidades:
                        lista_habilidades.append(habilidade)

                # Retorna a lista atualizada de habilidades
                return lista_habilidades
            
            return {"status": "Erro", "mensagem": "Formato inválido para as habilidades"}

        except Exception as e:
            # Retorna uma mensagem de erro se ocorrer uma exceção
            return {"status": "Erro", "mensagem": f"Erro ao processar a requisição POST: {str(e)}"}

    # Método PUT
    def put(self, id):
        try:
            # Converte os dados da requisição para JSON
            dados = json.loads(request.data)

            # Verifica se os dados são uma string
            if isinstance(dados, str):
                global lista_habilidades

                # Verifica se o ID é válido
                if 0 <= id < len(lista_habilidades):
                    # Atualiza a habilidade na posição especificada
                    lista_habilidades[id] = dados
                    return {"status": "Sucesso!", "mensagem": f"Habilidade na posição {id} atualizada"}

                return {"status": "Erro", "mensagem": "ID de habilidade inválido"}

            return {"status": "Erro", "mensagem": "Formato inválido para a habilidade"}

        except Exception as e:
            # Retorna uma mensagem de erro se ocorrer uma exceção
            return {"status": "Erro", "mensagem": f"Erro ao processar a requisição PUT: {str(e)}"}

    # Método DELETE
    def delete(self, id):
        # Verifica se o ID é válido
        if 0 <= id < len(lista_habilidades):
            # Remove a habilidade na posição especificada
            habilidade_removida = lista_habilidades.pop(id)
            return {"status": "Sucesso!", "mensagem": f"Habilidade '{habilidade_removida}' removida"}
        
        return {"status": "Erro", "mensagem": "ID de habilidade inválido"}
