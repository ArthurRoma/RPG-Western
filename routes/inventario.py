from flask import Blueprint, render_template, request
from database.models.inventario import Inventario

inventario_route = Blueprint("inventario", __name__)

'''CRUD Alvoro'''
@inventario_route.route("/luby", methods=["GET"])
def luby_home():
    return render_template("luby/index_luby.html")

@inventario_route.route("/cristian", methods=["GET"])
def cristian_home():
    return render_template("cristian/index_cristian.html")

@inventario_route.route("/nirco", methods=["GET"])
def nirco_home():
    return render_template("nirco/index_nirco.html")

@inventario_route.route("/alvoro", methods=["GET"])
def alvoro_home():
    return render_template("index.html")

@inventario_route.route("/")
def voltar():
    return render_template("pagina_principal.html")

@inventario_route.route("/lista")
def lista_inventario():
    inventarios = Inventario.select()
    return render_template("lista_inventario.html", inventarios=inventarios)



@inventario_route.route("/", methods=["POST"])
def inserir_inventario():
    data = request.json
    novo_inventario = Inventario.create(
        item = data['item'],
        quantidade = data['quantidade'],
        descricao = data['descricao'],
    )
    return render_template('item_inventario.html', inventario=novo_inventario)

@inventario_route.route("/new", methods=["GET"])
def form_inventario():
    return render_template('inventario_form.html')

@inventario_route.route("/<int:inventario_id>/edit")
def form_edit_inventario(inventario_id):
    inventario = Inventario.get_by_id(inventario_id)
    return render_template('inventario_form.html', inventario=inventario)

@inventario_route.route("/<int:inventario_id>/update", methods=["PUT"])
def update_item(inventario_id):
    inventario_editado = Inventario.get_by_id(inventario_id)
    data = request.json
    #obter usuário pelo id:
    inventario_editado.item = data['item']
    inventario_editado.quantidade = data['quantidade']
    inventario_editado.descricao = data['descricao']
    inventario_editado.save()
    #editar usuario
    return render_template('item_inventario.html', inventario=inventario_editado)

@inventario_route.route("/<int:inventario_id>", methods=["DELETE"])
def deletar_item(inventario_id):
    inventario = Inventario.get_by_id(inventario_id)
    inventario.delete_instance()
    return {'deleted': 'ok'}





