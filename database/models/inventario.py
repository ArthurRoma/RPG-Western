from peewee import Model, CharField, TextField, ForeignKeyField 
from database.database import db

class Inventario(Model):
    item = CharField()
    quantidade = CharField()
    descricao = TextField()

    class Meta:
        database = db

class Luby(Model):
    item = CharField()
    quantidade = CharField()
    descricao = TextField()

    class Meta:
        database = db

class Cristian(Model):
    item = CharField()
    quantidade = CharField()
    descricao = TextField()

    class Meta:
        database = db
 
class Nirco(Model):
    item = CharField()
    quantidade = CharField()
    descricao = TextField()

    class Meta:
        database = db
