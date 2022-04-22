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
@works_blueprint.route("/works/new", methods=['GET'])
def add_work():
    return render_template(
        "works/new.html",
        museums = museum_repository.select_all()
        )

# CREATE
# POST '/works'
@works_blueprint.route("/works", methods=['POST'])
def construct_work():
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    museum = museum_repository.select(request.form['museum_id'])
    work = Work(title, artist, year, museum)
    work_repository.save(work)
    return redirect("/works")

# SHOW
# GET '/works/<id>'

# EDIT
# GET '/works/<id>/edit'

# UPDATE
# PUT '/works/<id>'

# DELETE
# DELETE '/works/<id>'

