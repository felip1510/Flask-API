
#CONTÉM OS MODELOS QUE REPRESENTAM AS ENTIDADES DO BANCO
#BOOK REPRESENTA ENTIDADE BOOK

from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Book(db.Model):
#Indicar que 'book' é o modelo e ele é gerenciado pelo SQLAlchemy
    __tablename__ = "book"
    #define o nome da tabela
    id = db.Column(
        UUID(as_uuid=True),
        primary_key = True,
        default = uuid4
    )
    title = db.Column(
        String(255), #recebe a string
        nullable = False #não aceita nulo
    )
    author = db.Column(
        String(255),
        nullable = False
    )
    #title e author são obrigatórios
    description = db.Column(
        Text, #textos maiores
        nullable = False
    )

    is_favorite = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    is_reading = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    is_finished = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    #Transformando o modelo em dicionário
    '''
    Por isso, será criado um método responsável
    por transformar o 
    objeto 'book' em um dicionário python

    Quando ocorrer uma consulta ao nosso sistema ele retorna um objeto book
    ele não é simplesmente um dict python.
    O método AS_DICT() funciona como uma camada de conversão, selecionando
    apenas o necessário para ser exposto pela api e transformando em um DICT,
    estrutura que pode ser facilmente serializada para JSON resposta http.
    '''

    def as_dict(self):
        return{
            "id": str(self.id),
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "is_favorite": self.is_favorite,
            "is_reading": self.is_reading,
            "is_finished": self.is_finished
        }