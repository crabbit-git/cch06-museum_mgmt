from db.run_sql import run_sql

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

def select(id):
    sql = "SELECT * FROM works WHERE id = %s"
    values = [id]
    selection = run_sql(sql, values)[0]
    if selection is not None:
        return Work(
            selection['title'],
            selection['artist'],
            selection['year'],
            museum_repository.select(selection['museum_id']),
            selection['id']
        )

def update(work):
    sql = """
    UPDATE works
    SET (title, artist, year, museum_id) = (%s, %s, %s, %s)
    WHERE id = %s
    """
    values = [work.title, work.artist, work.year, work.museum.id, work.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM works WHERE id = %s"
    values = [id]
    run_sql(sql, values)
