from flask import Blueprint, render_template, request
from database.models.inventario import Luby
luby_route = Blueprint("luby", __name__)

'''CRUD LUBY'''

@luby_route.route("/lista")
def lista_luby():
    lubys = Luby.select()
    return render_template("luby/lista_luby.html", lubys=lubys)

@luby_route.route("/", methods=["POST"])
def inserir_luby():
    data = request.json
    novo_luby = Luby.create(
        item = data['item'],
        quantidade = data['quantidade'],
        descricao = data['descricao'],
    )
    return render_template("luby/item_luby.html", luby=novo_luby)

@luby_route.route("/new", methods=["GET"])
def form_luby():
    return render_template("luby/luby_form.html")

@luby_route.route("/<int:luby_id>/edit")
def form_edit_luby(luby_id):
    luby = Luby.get_by_id(luby_id)
    return render_template("luby/luby_form.html", luby=luby)

@luby_route.route("/<int:luby_id>/update", methods=["PUT"])
def update_luby(luby_id):
    luby_editado = Luby.get_by_id(luby_id)
    data = request.json
    luby_editado.item = data['item']
    luby_editado.quantidade = data['quantidade']
    luby_editado.descricao = data['descricao']
    luby_editado.save()
    return render_template("luby/item_luby.html", luby=luby_editado)

@luby_route.route("/<int:luby_id>", methods=['DELETE'])
def deletar_luby(luby_id):
    luby = Luby.get_by_id(luby_id)
    luby.delete_instance()
    return {'deleted' : 'ok'}

