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

# CREATE
# POST '/museums'

# SHOW
# GET '/museums/<id>'

# EDIT
# GET '/museums/<id>/edit'

# UPDATE
# PUT '/museums/<id>'

# DELETE
# DELETE '/museums/<id>'

