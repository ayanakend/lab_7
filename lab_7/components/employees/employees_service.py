from lab_7.utils import json_service


def create_employee(name, position, contacts):
    db = json_service.get_database()

    employee_id = len(db["employees"]) + 1
    employee = {"id": employee_id, "name": name, "position": position, "contacts": contacts}
    db["employees"].append(employee)
    json_service.set_database(db)

    return employee


def get_employee_by_id(employee_id):
    db = json_service.get_database()

    for employee in db["employees"]:
        if employee["id"] == employee_id:
            return employee

    return {"message": f"Работник с id {employee_id} не найден"}


def update_employee_by_id(employee_id, new_data):
    db = json_service.get_database()

    for i, employee in enumerate(db["employees"]):
        if employee["id"] == employee_id:
            employee.update(new_data)
            json_service.set_database(db)
            return employee

    return {"message": f"Работник с id {employee_id} не найден"}


def delete_employee_by_id(employee_id):
    db = json_service.get_database()

    for i, employee in enumerate(db["employees"]):
        if employee["id"] == employee_id:
            deleted_employee = db["employees"].pop(i)
            json_service.set_database(db)
            return deleted_employee

    return {"message": f"Работник с id {employee_id} не найден"}
