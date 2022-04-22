from db.run_sql import run_sql

from models.work import Work
from models.museum import Museum

# Write your functions here
def save(museum):
    sql = """
    INSERT INTO museums (name, address)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [
        museum.name,
        museum.address
        ]
    insertion = run_sql(sql, values)
    museum.id = insertion[0]['id']
    return museum

def select_all():
    sql = "SELECT * FROM museums"
    selection = run_sql(sql)
    return [Museum(
        museum['name'],
        museum['address'],
        museum['id']
        ) for museum in selection]

def select(id):
    sql = "SELECT * FROM museums WHERE id = %s"
    values = [id]
    selection = run_sql(sql, values)[0]
    if selection is not None:
        return Museum(
            selection['name'],
            selection['address'],
            selection['id']
        )

def update(museum):
    sql = """
    UPDATE museums
    SET (name, address) = (%s, %s)
    WHERE id = %s
    """
    values = [museum.name, museum.address, museum.id]
    run_sql(sql, values)
