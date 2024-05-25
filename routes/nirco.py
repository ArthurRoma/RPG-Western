from flask import Blueprint, render_template, request
from database.models.inventario import Nirco
nirco_route = Blueprint("nirco", __name__)

'''CRUD Crisitan'''

@nirco_route.route("/lista")
def lista_nirco():
    nircos = Nirco.select()
    return render_template("nirco/lista_nirco.html", nircos=nircos)

@nirco_route.route("/", methods=["POST"])
def inserir_nirco():
    data = request.json
    novo_nirco = Nirco.create(
        item = data['item'],
        quantidade = data['quantidade'],
        descricao = data['descricao'],
    )
    return render_template("nirco/item_nirco.html", nirco=novo_nirco)

@nirco_route.route("/new", methods=["GET"])
def form_nirco():
    return render_template("nirco/nirco_form.html")

@nirco_route.route("/<int:nirco_id>/edit")
def form_edit_nirco(nirco_id):
    nirco = Nirco.get_by_id(nirco_id)
    return render_template("nirco/nirco_form.html", nirco=nirco)

@nirco_route.route("/<int:nirco_id>/update", methods=["PUT"])
def update_nirco(nirco_id):
    nirco_editado = Nirco.get_by_id(nirco_id)
    data = request.json
    nirco_editado.item = data['item']
    nirco_editado.quantidade = data['quantidade']
    nirco_editado.descricao = data['descricao']
    nirco_editado.save()
    return render_template("nirco/item_nirco.html", nirco=nirco_editado)

@nirco_route.route("/<int:nirco_id>", methods=['DELETE'])
def deletar_nirco(nirco_id):
    nirco = Nirco.get_by_id(nirco_id)
    nirco.delete_instance()
    return {'deleted' : 'ok'}

