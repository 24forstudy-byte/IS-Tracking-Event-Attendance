from models.place import Place, get_all_places, get_place_by_id
from models.event_type import EventType, get_all_event_types, get_event_type_by_id
from models.staff import Staff, get_all_staffs


def menu_references():
    """Главное меню справочников"""
    while True:
        print("\n=== Справочники 📖 ===")
        print("1. Управление местами")
        print("2. Управление типами мероприятий")
        print("3. Управление персоналом")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            menu_place()
        elif choice == "2":
            menu_event_type()
        elif choice == "3":
            menu_staff()
        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")


def menu_place():
    """Меню управления местами"""
    while True:
        print("\n=== Места 📍 ===")
        print("1. Показать все места")
        print("2. Добавить место")
        print("3. Обновить место")
        print("4. Удалить место")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            places = get_all_places()
            print("\nСписок мест:")
            for p in places:
                print(f"{p.PlaceID}. Название: {p.Title}\nАдрес: {p.Address}")

        elif choice == "2":
            print("\n=== Добавление нового места ===")
            title = input("Название: ")
            address = input("Адрес: ")
            place = Place(Title=title, Address=address)
            place.save()
            print("Место добавлено! 👍")

        elif choice == "3":
            place_id = int(input("Введите ID места для обновления: "))
            current = get_place_by_id(place_id)
            if not current:
                print("Место не найдено. ⛔")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")
            title = input("Новое название: ")
            address = input("Новый адрес: ")

            place = Place(
                PlaceID=place_id,
                Title=title if title else current.Title,
                Address=address if address else current.Address
            )
            place.save()
            print("Место обновлено! 🖌️")

        elif choice == "4":
            place_id = int(input("Введите ID места для удаления: "))
            p = get_place_by_id(place_id)
            if not p:
                print("Место не найдено. ⛔")
            else:
                place = Place(PlaceID=place_id)
                place.delete()
                print("Место удалено! ❌")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")


def menu_event_type():
    """Меню управления типами мероприятий"""
    while True:
        print("\n=== Типы мероприятий 🏷️  ===")
        print("1. Показать все типы")
        print("2. Добавить тип")
        print("3. Обновить тип")
        print("4. Удалить тип")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            types = get_all_event_types()
            print("\nСписок типов мероприятий:")
            for t in types:
                print(f"{t.EventTypeID}. Название: {t.Title}")

        elif choice == "2":
            print("\n=== Добавление нового типа ===")
            title = input("Название типа: ")
            event_type = EventType(Title=title)
            event_type.save()
            print("Тип добавлен! 👍")

        elif choice == "3":
            type_id = int(input("Введите ID типа для обновления: "))
            current = get_event_type_by_id(type_id)
            if not current:
                print("Тип не найден. ⛔")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")
            title = input("Новое название: ")
            event_type = EventType(
                EventTypeID=type_id,
                Title=title if title else current.Title
            )
            event_type.save()
            print("Тип обновлён! 🖌️")

        elif choice == "4":
            type_id = int(input("Введите ID типа для удаления: "))
            t = get_event_type_by_id(type_id)
            if not t:
                print("Тип мероприятий не найден. ⛔")
            else:
                event_type = EventType(EventTypeID=type_id)
                event_type.delete()
                print("Тип удалён! ❌")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")


def menu_staff():
    """Меню управления персоналом"""
    while True:
        print("\n=== Персонал 👤 ===")
        print("1. Просмотреть данные персонала")
        print("2. Обновить данные персонала")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            staff_list = get_all_staffs()
            if not staff_list:
                print("Персонал ещё не создан.")
            else:
                for s in staff_list:
                    print(f"{s.StaffID}. ФИО: {s.FullName}\nТелефон: {s.Phone}\nПочта: {s.Mail}")

        elif choice == "2":
            staff_list = get_all_staffs()
            if not staff_list:
                print("Персонал не найден. Создание нового.")
                fullname = input("ФИО: ")
                phone = input("Телефон: ")
                mail = input("Почта: ")
                if not fullname or not phone or not mail:
                    print("Неверный ввод: все поля обязательны для заполнения.")
                    continue
                staff = Staff(FullName=fullname, Phone=phone, Mail=mail)
                staff.save()
                print("Персонал создан! 👍")
            else:
                s = staff_list[0]
                print("\nОставьте поле пустым, чтобы не изменять значение")
                fullname = input("Новое ФИО: ")
                phone = input("Новый телефон: ")
                mail = input("Новая почта: ")
                updated = Staff(
                    StaffID=s.StaffID,
                    FullName=fullname if fullname else s.FullName,
                    Phone=phone if phone else s.Phone,
                    Mail=mail if mail else s.Mail
                )
                updated.save()
                print("Данные обновлены! 🖌️")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")
