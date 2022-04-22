from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository
import repositories.work_repository as work_repository

works_blueprint = Blueprint("works", __name__)

# INDEX
# GET '/works
@works_blueprint.route("/works")
def works():
    return render_template(
        "works/index.html",
        works = work_repository.select_all()
        )

# NEW
# GET '/works/new'

# CREATE
# POST '/works'

# SHOW
# GET '/works/<id>'

# EDIT
# GET '/works/<id>/edit'

# UPDATE
# PUT '/works/<id>'

# DELETE
# DELETE '/works/<id>'

