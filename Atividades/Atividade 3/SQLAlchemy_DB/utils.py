from models import Programador, Habilidades, Programador_Habilidade, db_session

def insere_programador():
    programador = Programador(nome="Daniel", idade=19, email="DanielDev@email.com")
    print(f"Programador inserido com sucesso: {programador}")
    programador.save_programador()



def insere_habilidades():
    habilidades = Habilidades(nome="Python, Java")
    print(f"Habiliade(s) inserida(s) com sucesso: {habilidades}")
    habilidades.save_habilidades()

def insere_programador_habilidade():
    programador = Programador.query.first()
    habilidades = Habilidades.query.first()

    if programador and habilidades:
        programador_habilidade = Programador_Habilidade(programador_id=programador.id, habilidades_id=habilidades.id)
        print(f"Relação Programador e Habilidades inseridos com sucesso: {programador_habilidade}")
        programador_habilidade.save_programador_habilidade()
    else:
        print("Programador ou Habilidades não encontrados.")

def consulta_programadores():
    programadores = db_session.query(Programador).all()
    for programador in programadores:
        print(programador)

def consulta_habilidades():
    habilidades = db_session.query(Habilidades).all()
    for habilidade in habilidades:
        print(habilidade)

def consulta_programadores_habilidades():
    programadores_habilidades = db_session.query(Programador_Habilidade).all()
    for ph in programadores_habilidades:
        print(ph)

def altera_programador(id, nome, idade, email):
    programador = db_session.query(Programador).filter_by(id=id).first()
    if programador:
        programador.nome = nome
        programador.idade = idade
        programador.email = email
        db_session.commit()
        print("Programador alterado com sucesso!")
    else:
        print("Programador não encontrado.")

def exclui_programador(id):
    programador = db_session.query(Programador).filter_by(id=id).first()
    if programador:
        db_session.delete(programador)
        db_session.commit()
        print("Programador excluído com sucesso!")
    else:
        print("Programador não encontrado.")

if __name__ == ("__main__"):
    # insere_programador()
    # insere_habilidades()
    # insere_programador_habilidade()

    # consulta_programadores()
    # consulta_habilidades()
    # consulta_programadores_habilidades()

    altera_programador(3, "Robson", 26, "rob.dev@email.com")
    consulta_programadores()

    # exclui_programador(5)
    # consulta_programadores()