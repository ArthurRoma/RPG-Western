from flask import Blueprint, render_template, request
from database.models.inventario import Cristian
cristian_route = Blueprint("cristian", __name__)

'''CRUD Crisitan'''

@cristian_route.route("/lista")
def lista_cristian():
    cristians = Cristian.select()
    return render_template("cristian/lista_cristian.html", cristians=cristians)

@cristian_route.route("/", methods=["POST"])
def inserir_cristian():
    data = request.json
    novo_cristian = Cristian.create(
        item = data['item'],
        quantidade = data['quantidade'],
        descricao = data['descricao'],
    )
    return render_template("cristian/item_cristian.html", cristian=novo_cristian)

@cristian_route.route("/new", methods=["GET"])
def form_cristian():
    return render_template("cristian/cristian_form.html")

@cristian_route.route("/<int:cristian_id>/edit")
def form_edit_cristian(cristian_id):
    cristian = Cristian.get_by_id(cristian_id)
    return render_template("cristian/cristian_form.html", cristian=cristian)

@cristian_route.route("/<int:cristian_id>/update", methods=["PUT"])
def update_cristian(cristian_id):
    cristian_editado = Cristian.get_by_id(cristian_id)
    data = request.json
    cristian_editado.item = data['item']
    cristian_editado.quantidade = data['quantidade']
    cristian_editado.descricao = data['descricao']
    cristian_editado.save()
    return render_template("cristian/item_cristian.html", cristian=cristian_editado)

@cristian_route.route("/<int:cristian_id>", methods=['DELETE'])
def deletar_cristian(cristian_id):
    cristian = Cristian.get_by_id(cristian_id)
    cristian.delete_instance()
    return {'deleted' : 'ok'}

