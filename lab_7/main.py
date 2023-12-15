from lab_7.components.trains.train_service import (
    get_all_trains,
    get_train_by_id,
    create_train,
    update_train_by_id,
    delete_train_by_id,
    create_ticket,
    get_ticket_by_id,
    update_ticket_by_id,
    delete_ticket_by_id,
)
from lab_7.components.passengers.passengers_service import (
    create_passenger,
    get_passenger_by_id,
    update_passenger_by_id,
    delete_passenger_by_id,
)


def display_menu():
    print("Меню:")
    print("1. Получить информацию о поезде")
    print("2. Получить информацию о билете")
    print("3. Создать билет")
    print("4. Обновить информацию о билете")
    print("5. Удалить билет")
    print("6. Создать пассажира")
    print("7. Получить информацию о пассажире")
    print("8. Обновить информацию о пассажире")
    print("9. Удалить пассажира")
    print("10. Создать поезд")
    print("11. Обновить информацию о поезде")
    print("12. Удалить поезд")
    print("0. Выход")


def get_valid_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        if input_type == "number" and user_input.isdigit():
            return int(user_input)
        elif input_type == "text" and user_input.isalpha():
            return user_input
        else:
            print("Неверный формат ввода. Пожалуйста, введите корректное значение.")


def main():
    while True:
        display_menu()
        choice = get_valid_input("Выберите действие (введите цифру): ", "number")

        if choice == 0:
            print("Выход из программы.")
            break
        elif choice == 1:
            train_id = get_valid_input("Введите ID поезда: ", "number")
            train_info = get_train_by_id(train_id)
            print(train_info)
        elif choice == 2:
            ticket_id = get_valid_input("Введите ID билета: ", "number")
            ticket_info = get_ticket_by_id(ticket_id)
            print(ticket_info)
        elif choice == 3:
            passenger_id = get_valid_input("Введите ID пассажира: ", "number")
            train_id = get_valid_input("Введите ID поезда: ", "number")
            price = get_valid_input("Введите цену билета: ", "number")
            ticket = create_ticket(passenger_id, train_id, price)
            print(f"Билет создан: {ticket}")
        elif choice == 4:
            ticket_id = get_valid_input("Введите ID билета для обновления: ", "number")
            new_price = get_valid_input("Введите новую цену билета: ", "number")
            new_data = {"price": new_price}
            updated_ticket = update_ticket_by_id(ticket_id, new_data)
            print(f"Билет обновлен: {updated_ticket}")
        elif choice == 5:
            ticket_id = get_valid_input("Введите ID билета для удаления: ", "number")
            deleted_ticket = delete_ticket_by_id(ticket_id)
            print(f"Билет удален: {deleted_ticket}")
        elif choice == 6:
            passenger_name = get_valid_input("Введите имя пассажира: ", "text")
            passenger_age = get_valid_input("Введите возраст пассажира: ", "number")
            passenger_email = get_valid_input("Введите email пассажира: ", "text")
            passenger_phone = get_valid_input("Введите телефон пассажира: ", "number")
            passenger = create_passenger(passenger_name, passenger_age, passenger_email)
            print(f"Пассажир создан: {passenger}")
        elif choice == 7:
            passenger_id = get_valid_input("Введите ID пассажира: ", "number")
            passenger_info = get_passenger_by_id(passenger_id)
            print(passenger_info)
        elif choice == 8:
            passenger_id = get_valid_input("Введите ID пассажира для обновления: ", "number")
            new_name = get_valid_input("Введите новое имя пассажира: ", "text")
            new_age = get_valid_input("Введите новый возраст пассажира: ", "number")
            new_email = get_valid_input("Введите новый email пассажира: ", "text")
            new_phone = get_valid_input("Введите новый телефон пассажира: ", "number")
            new_data = {"name": new_name, "age": new_age, "email": new_email, "phone": new_phone}
            updated_passenger = update_passenger_by_id(passenger_id, new_data)
            print(f"Пассажир обновлен: {updated_passenger}")
        elif choice == 9:
            passenger_id = get_valid_input("Введите ID пассажира для удаления: ", "number")
            deleted_passenger = delete_passenger_by_id(passenger_id)
            print(f"Пассажир удален: {deleted_passenger}")
        elif choice == 10:
            train_name = get_valid_input("Введите название поезда: ", "text")
            train_schedule = get_valid_input("Введите расписание поезда: ", "text")
            new_train = create_train(train_name, train_schedule)
            print(f"Поезд создан: {new_train}")
        elif choice == 11:
            train_id = get_valid_input("Введите ID поезда для обновления: ", "number")
            new_name = get_valid_input("Введите новое название поезда: ", "text")
            new_schedule = get_valid_input("Введите новое расписание поезда: ", "text")
            new_data = {"name": new_name, "schedule": new_schedule}
            updated_train = update_train_by_id(train_id, new_data)
            print(f"Поезд обновлен: {updated_train}")
        elif choice == 12:
            train_id = get_valid_input("Введите ID поезда для удаления: ", "number")
            deleted_train = delete_train_by_id(train_id)
            print(f"Поезд удален: {deleted_train}")
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")


if __name__ == "__main__":
    main()
