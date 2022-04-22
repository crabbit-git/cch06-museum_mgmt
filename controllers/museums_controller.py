from flask import render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
import repositories.museum_repository as museum_repository

museums_blueprint = Blueprint("museums", __name__)

# INDEX
# GET '/museums
@museums_blueprint.route("/museums")
def museums():
    return render_template(
        "museums/index.html",
        museums = museum_repository.select_all()
        )

# NEW
# GET '/museums/new'
@museums_blueprint.route("/museums/new", methods=['GET'])
def add_museum():
    return render_template(
        "museums/new.html",
        museums = museum_repository.select_all()
        )

# CREATE
# POST '/museums'
@museums_blueprint.route("/museums", methods=['POST'])
def construct_museum():
    name = request.form['name']
    address = request.form['address']
    museum = Museum(name, address)
    museum_repository.save(museum)
    return redirect("/museums")

# SHOW
# GET '/museums/<id>'
@museums_blueprint.route("/museums/<id>", methods=['GET'])
def museum_info(id):
    return render_template(
        "museums/info.html",
        museum = museum_repository.select(id)
        )

# EDIT
# GET '/museums/<id>/edit'
@museums_blueprint.route("/museums/<id>/edit", methods=['GET'])
def edit_museum(id):
    return render_template(
        "museums/edit.html",
        museum = museum_repository.select(id)
        )

# UPDATE
# PUT '/museums/<id>'
@museums_blueprint.route("/museums/<id>", methods=['POST'])
def update_museum(id):
    name = request.form['name']
    address = request.form['address']
    museum = Museum(name, address, id)
    museum_repository.update(museum)
    return redirect("/museums")

# DELETE
# DELETE '/museums/<id>'
@museums_blueprint.route("/museums/<id>/delete", methods=['POST'])
def delete_museum(id):
    museum_repository.delete(id)
    return redirect("/museums")
