from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///atividades_5.db') # atividade_5 da Atividade 5
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')
    status = Column(String(20))

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()