from db.run_sql import run_sql

from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository

# Write your functions here
def save(work):
    sql = """
    INSERT INTO works (title, artist, year, museum_id)
    VALUES (%s, %s, %s, %s)
    RETURNING id
    """
    values = [
        work.title,
        work.artist,
        work.year,
        work.museum.id
        ]
    insertion = run_sql(sql, values)
    work.id = insertion[0]['id']
    return work

def select_all():
    sql = "SELECT * FROM works"
    selection = run_sql(sql)
    return [Work(
        work['title'],
        work['artist'],
        work['year'],
        museum_repository.select(work['museum_id']),
        work['id']
        ) for work in selection]
