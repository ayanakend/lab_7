import lab_7.utils.json_service as json_service


def get_train_by_id(train_id):
    db = json_service.get_database()

    for train in db["trains"]:
        if train["id"] == train_id:
            return train

    return {"message": f"Поезд с id {train_id} не найден"}


def get_all_trains():
    db = json_service.get_database()
    return db["trains"]


def create_train(name, schedule):
    db = json_service.get_database()

    train_id = len(db["trains"]) + 1
    train = {"id": train_id, "name": name, "schedule": schedule, "passengers": []}
    db["trains"].append(train)
    json_service.set_database(db)

    return train


def update_train_by_id(train_id, new_data):
    db = json_service.get_database()

    for i, train in enumerate(db["trains"]):
        if train["id"] == train_id:
            train.update(new_data)
            json_service.set_database(db)
            return train

    return {"message": f"Поезд с id {train_id} не найден"}


def delete_train_by_id(train_id):
    db = json_service.get_database()

    for i, train in enumerate(db["trains"]):
        if train["id"] == train_id:
            deleted_train = db["trains"].pop(i)
            json_service.set_database(db)
            return deleted_train

    return {"message": f"Поезд с id {train_id} не найден"}


def create_ticket(passenger_id, train_id, price):
    db = json_service.get_database()

    ticket_id = len(db["tickets"]) + 1
    ticket = {"id": ticket_id, "passenger_id": passenger_id, "train_id": train_id, "price": price}
    db["tickets"].append(ticket)
    json_service.set_database(db)

    return ticket


def get_ticket_by_id(ticket_id):
    db = json_service.get_database()

    for ticket in db["tickets"]:
        if ticket["id"] == ticket_id:
            return ticket

    return {"message": f"Билет с id {ticket_id} не найден"}


def update_ticket_by_id(ticket_id, new_data):
    db = json_service.get_database()

    for i, ticket in enumerate(db["tickets"]):
        if ticket["id"] == ticket_id:
            ticket.update(new_data)
            json_service.set_database(db)
            return ticket

    return {"message": f"Билет с id {ticket_id} не найден"}


def delete_ticket_by_id(ticket_id):
    db = json_service.get_database()

    for i, ticket in enumerate(db["tickets"]):
        if ticket["id"] == ticket_id:
            deleted_ticket = db["tickets"].pop(i)
            json_service.set_database(db)
            return deleted_ticket

    return {"message": f"Билет с id {ticket_id} не найден"}
