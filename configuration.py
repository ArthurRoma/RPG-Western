from flask import Flask
from database.database import db
from database.models.inventario import Inventario
from database.models.inventario import Luby
from database.models.inventario import Cristian
from database.models.inventario import Nirco
from routes.home import home_route
from routes.inventario import inventario_route
from routes.luby import luby_route
from routes.cristian import cristian_route
from routes.nirco import nirco_route
from peewee import PostgresqlDatabase

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(inventario_route, url_prefix="/inventario")
    app.register_blueprint(luby_route, url_prefix="/luby")
    app.register_blueprint(cristian_route, url_prefix="/cristian")
    app.register_blueprint(nirco_route, url_prefix="/nirco")
    
def configure_db():
    db.connect()
    db.create_tables([Inventario])
    db.create_tables([Luby])
    db.create_tables([Cristian])
    db.create_tables([Nirco])