# from lab_7.utils import json_service
#
#
# def create_ticket(passenger_id, train_id, price):
#     db = json_service.get_database()
#
#     ticket_id = len(db["tickets"]) + 1
#     ticket = {"id": ticket_id, "passenger_id": passenger_id, "train_id": train_id, "price": price}
#     db["tickets"].append(ticket)
#     json_service.set_database(db)
#
#     return ticket
#
#
# def get_ticket_by_id(ticket_id):
#     db = json_service.get_database()
#
#     for ticket in db["tickets"]:
#         if ticket["id"] == ticket_id:
#             return ticket
#
#     return {"message": f"Билет с id {ticket_id} не найден"}
#
#
# def update_ticket_by_id(ticket_id, new_data):
#     db = json_service.get_database()
#
#     for i, ticket in enumerate(db["tickets"]):
#         if ticket["id"] == ticket_id:
#             ticket.update(new_data)
#             json_service.set_database(db)
#             return ticket
#
#     return {"message": f"Билет с id {ticket_id} не найден"}
#
#
# def delete_ticket_by_id(ticket_id):
#     db = json_service.get_database()
#
#     for i, ticket in enumerate(db["tickets"]):
#         if ticket["id"] == ticket_id:
#             deleted_ticket = db["tickets"].pop(i)
#             json_service.set_database(db)
#             return deleted_ticket
#
#     return {"message": f"Билет с id {ticket_id} не найден"}
