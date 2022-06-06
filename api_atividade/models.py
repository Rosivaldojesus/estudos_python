from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividade.db', echo=True, future=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    # Função de adicionar ou alterar pessoa
    def save(pessoa):
        db_session.add(pessoa)
        db_session.commit()

    # Função de exluí pessoa
    def delete(pessoa):
        db_session.delete(pessoa)
        db_session.commit()

class Atividade(Base):
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    # Função de adicionar ou alterar pessoa
    def save(self):
        db_session.add(self)
        db_session.commit(self)

    # Função de exluí pessoa
    def delete(self):
        db_session.delete(self)
        db_session.commit(self)



def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()

