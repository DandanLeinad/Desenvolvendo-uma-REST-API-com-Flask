from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///atividades.db", echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Programador(Base):
    __tablename__ = "programador"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(20))
    idade = Column(Integer)
    email = Column(String(25))

    programador_habilidade = relationship("Programador_Habilidade", back_populates="programador")

    def __repr__(self):
        return f"<Programador(nome={self.nome}, idade={self.idade}, email={self.email})>"
    
    def save_programador(self):
        db_session.add(self)
        db_session.commit()

class Habilidades(Base):
    __tablename__ = "habilidades"
    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String(20))

    # Corrigir o relacionamento com back_populates
    programador_habilidade = relationship("Programador_Habilidade", back_populates="habilidade")
    
    def __repr__(self):
        return f"<Habilidades(nome={self.nome})>"
    
    def save_habilidades(self):
        db_session.add(self)
        db_session.commit()

class Programador_Habilidade(Base):
    __tablename__ = "programador_habilidade"
    id = Column(Integer, primary_key=True, nullable=False)
    programador_id = Column(Integer, ForeignKey("programador.id"))
    habilidades_id = Column(Integer, ForeignKey("habilidades.id"))

    programador = relationship("Programador", back_populates="programador_habilidade")
    habilidade = relationship("Habilidades", back_populates="programador_habilidade")

    def __repr__(self):
        return f"<Programador_Habilidade(programador_id={self.programador_id}, habilidades_id={self.habilidades_id})>"
    
    def save_programador_habilidade(self):
        db_session.add(self)
        db_session.commit()
        
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == ("__main__"):
    init_db()
