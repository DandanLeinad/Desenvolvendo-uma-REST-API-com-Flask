from classes_tabelas import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Daniel',idade=20)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    # Verifica se a pessoa 'Rafael' existe
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()

    if pessoa:
        print(pessoa.idade)
    else:
        print("Pessoa  não encontrada.")


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

# def insere_usuario(login, senha):
#     usuario = Usuarios(login=login, senha=senha)
#     usuario.save()

# def consulta_todos_usuarios():
#     usuarios = Usuarios.query.all()
#     print(usuarios)

if __name__ == '__main__':
    #insere_usuario('rafael', '1234')
    #insere_usuario('galleani', '4321')
    #consulta_todos_usuarios()
    insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()