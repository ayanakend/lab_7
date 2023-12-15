from lab_7.utils import json_service


def create_passenger(name, age, contacts):
    db = json_service.get_database()

    passenger_id = len(db["passengers"]) + 1
    passenger = {"id": passenger_id, "name": name, "age": age, "contacts": contacts}
    db["passengers"].append(passenger)
    json_service.set_database(db)

    return passenger


def get_passenger_by_id(passenger_id):
    db = json_service.get_database()

    for passenger in db["passengers"]:
        if passenger["id"] == passenger_id:
            return passenger

    return {"message": f"Пассажир с id {passenger_id} не найден"}


def update_passenger_by_id(passenger_id, new_data):
    db = json_service.get_database()

    for i, passenger in enumerate(db["passengers"]):
        if passenger["id"] == passenger_id:
            passenger.update(new_data)
            json_service.set_database(db)
            return passenger

    return {"message": f"Пассажир с id {passenger_id} не найден"}


def delete_passenger_by_id(passenger_id):
    db = json_service.get_database()

    for i, passenger in enumerate(db["passengers"]):
        if passenger["id"] == passenger_id:
            deleted_passenger = db["passengers"].pop(i)
            json_service.set_database(db)
            return deleted_passenger

    return {"message": f"Пассажир с id {passenger_id} не найден"}
