from models.event import Event, get_all_events, get_event_by_id
from models.event_type import get_all_event_types, get_event_type_by_id
from models.place import get_all_places, get_place_by_id

def menu_event():
    while True:
        print("\n=== Мероприятия 🎪 ===")
        print("1. Показать все мероприятия")
        print("2. Добавить мероприятие")
        print("3. Обновить мероприятие")
        print("4. Удалить мероприятие")
        print("5. Архивировать мероприятие")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            events = get_all_events()
            print("\nСписок мероприятий:")
            for e in events:
                print(f"{e.EventID}. Тип: {e.EventTypeID} | Место: {e.PlaceID} | "
                      f"Название: {e.Title} | Дата: {e.DateTime} | Статус: {e.Status}")

        elif choice == "2":
            print("\n=== Добавление нового мероприятия ===")
            title = input("Название мероприятия: ")
            date_time = input("Дата и время (%Y-%m-%d %H:%M): ")
            status = "Приём заявок"   

            # Выбор типа мероприятия
            print("\nДоступные типы мероприятия:")
            event_types = get_all_event_types()
            for t in event_types:
                print(f"{t.EventTypeID} - {t.Title}")
            type_id = int(input("Введите ID типа мероприятия: "))
            if get_event_type_by_id(type_id) is None:
                print("Тип мероприятия с таким ID не найден. ⛔")
                continue

            # Выбор места
            print("\nДоступные места:")
            places = get_all_places()
            for p in places:
                print(f"{p.PlaceID} - {p.Title}")
            place_id = int(input("Введите ID места: "))
            if get_place_by_id(place_id) is None:
                print("Место с таким ID не найдено. ⛔")
                continue

            event = Event(
                EventTypeID=type_id,
                PlaceID=place_id,
                Title=title,
                DateTime=date_time,
                Status=status
            )
            event.save()
            print("Мероприятие добавлено! 👍")

        elif choice == "3":
            id_to_update = int(input("Введите ID мероприятия для обновления: "))
            current_event = next((e for e in get_all_events() if e.EventID == id_to_update), None)
            if not current_event:
                print("Мероприятие не найдено. ⛔")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")
            title = input("Новое название: ")
            date_time = input("Новая дата и время (%Y-%m-%d %H:%M): ")

            # Выбор типа мероприятия
            print(f"\nТекущий тип мероприятия ID: {current_event.EventTypeID}")
            print("Доступные типы мероприятия:")
            for t in get_all_event_types():
                print(f"{t.EventTypeID} - {t.Title}")
            type_id_str = input("Введите новый ID типа: ")
            if get_event_type_by_id(type_id) is None:
                print("Тип мероприятия с таким ID не найден. ⛔")
                continue

            # Выбор места
            print(f"\nТекущее место ID: {current_event.PlaceID}")
            print("Доступные места:")
            for p in get_all_places():
                print(f"{p.PlaceID} - {p.Title}")
            place_id_str = input("Введите новый ID места: ")
            if get_place_by_id(place_id) is None:
                print("Место с таким ID не найдено. ⛔")
                continue

            
            event = Event(
                EventID=id_to_update,  
                EventTypeID=int(type_id_str) if type_id_str else current_event.EventTypeID,
                PlaceID=int(place_id_str) if place_id_str else current_event.PlaceID,
                Title=title if title else current_event.Title,
                DateTime=date_time if date_time else current_event.DateTime,
                Status=current_event.Status  
            )
            event.save()
            print("Мероприятие обновлено! 🖌️")

        elif choice == "4":
            id_to_delete = int(input("Введите ID мероприятия для удаления: "))
            event = get_event_by_id(id_to_delete)          
            if not event:
                print("Мероприятие не найдено. ⛔")
                continue

            if event.Status == "Архивировано":
                print("Нельзя удалить архивированное мероприятие. ⛔")
                continue
                
            event.delete()
            print("Мероприятие удалено! ❌")

        elif choice == "5":
            print("\n=== Архивирование мероприятия ===")
            id_to_archive = int(input("Введите ID мероприятия для архивирования: "))
            event = get_event_by_id(id_to_archive)
            if not event:
                print("Мероприятие не найдено. ⛔")
            else:
                event.archive()
                print("Мероприятие архивировано!👍")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")