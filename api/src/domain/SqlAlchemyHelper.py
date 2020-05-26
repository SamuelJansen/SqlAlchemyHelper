from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, UnicodeText, MetaData, Sequence, DateTime

UnicodeText = UnicodeText
DateTime = DateTime

Table = Table
Column = Column
Integer = Integer
String = String

relationship = relationship

Sequence = Sequence
ForeignKey = ForeignKey
MetaData = MetaData

Base = declarative_base()

class SqlAlchemyHelper:

    DEFAULT_DATABASE_TYPE = 'sqlite'
    TRIPLE_BAR = '///'
    EXTENSION = 'db'

    def __init__(self,globals,name,type=DEFAULT_DATABASE_TYPE,extension=EXTENSION):
        self.globals = globals
        self.name = name
        self.type = type
        self.extension = extension
        self.engine = create_engine(f'{self.type}:{self.TRIPLE_BAR}{self.name}.{self.extension}', echo=False)
        self.session = scoped_session(sessionmaker(self.engine)) ###- sessionmaker(bind=self.engine)()
        Base.metadata.bind = self.engine

    def run(self):
        Base.metadata.create_all(self.engine)
