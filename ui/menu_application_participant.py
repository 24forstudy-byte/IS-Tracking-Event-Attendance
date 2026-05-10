from models.application import Application, get_all_applications, get_application_by_id
from models.participant import Participant, get_all_participants, get_participant_by_id
from models.event import get_all_events, get_event_by_id
from models.staff import get_staff_by_id
from datetime import datetime

def menu_participant():
    """Меню управления участниками"""

    while True:
        print("\n=== Участники 👥 ===")
        print("1. Показать всех участников")
        print("2. Добавить участника")
        print("3. Обновить участника")
        print("4. Удалить участника")
        print("5. Получить участника")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            participants = get_all_participants()
            print("\nСписок участников:")
            for p in participants:
                print(f"{p.ParticipantID}. ФИО: {p.FullName} | Телефон: {p.Phone} | Почта: {p.Mail}")

        elif choice == "2":
            print("\n=== Добавление нового участника ===")
            fullname = input("ФИО: ")
            phone = input("Телефон: ")
            mail = input("Почта: ")
            participant = Participant(
                FullName=fullname,
                Phone=phone,
                Mail=mail
            )
            participant.save()
            print("Участник добавлен!👍")

        elif choice == "3":
            participant_id = int(input("Введите ID участника для обновления: "))
            current = get_participant_by_id(participant_id)
            if not current:
                print("Участник не найден. ⛔")
                continue

            print("\nОставьте поле пустым, чтобы не изменять значение")
            fullname = input("Новое ФИО: ")
            phone = input("Новый телефон: ")
            mail = input("Новая почта: ")

            participant = Participant(
                ParticipantID=participant_id,
                FullName=fullname if fullname else current.FullName,
                Phone=phone if phone else current.Phone,
                Mail=mail if mail else current.Mail
            )
            participant.save()
            print("Участник обновлён! 🖌️")

        elif choice == "4":
            participant_id = int(input("Введите ID участника для удаления: "))
            participant = Participant(ParticipantID=participant_id)
            participant.delete()
            print("Участник удалён! ❌")

        elif choice == "5":
            participant_id = int(input("Введите ID участника: "))
            p = get_participant_by_id(participant_id)
            if p:
                print(f"Участник найден! ФИО: {p.FullName} | телефон: {p.Phone} | почта: {p.Mail}")
            else:
                print("Участник не найден. ⛔")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")


def menu_application():
    """Меню управления заявками"""

    staff_list = get_all_staffs()
    if not staff_list:
        print("Нет персонала в базе. Сначала добавьте персонал через меню 'Справочники'.")
        return
    staff_id = staff_list[0].StaffID

    while True:
        print("\n=== Заявки 📋 ===")
        print("1. Показать все заявки")
        print("2. Зарегистрировать заявку")
        print("3. Получить заявку")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            applications = get_all_applications()
            print("\nСписок заявок:")
            for a in applications:
                print(f"{a.ApplicationID}. Участник: {a.ParticipantID} | "
                      f"Мероприятие: {a.EventID} | Сотрудник: {a.StaffID} | "
                      f"Дата: {a.DateTime}")

        elif choice == "2":
            # Выбор участника
            print("\nДоступные участники:")
            participants = get_all_participants()
            for p in participants:
                print(f"{p.ParticipantID}. {p.FullName}")
            participant_id = int(input("Введите ID участника: "))
            participant = get_participant_by_id(participant_id)
            if not participant:
                print("Участник не найден. ⛔")
                continue

            # Выбор мероприятия
            print("\nДоступные мероприятия:")
            all_events = get_all_events()
            active_events = [e for e in all_events if e.Status != "Архивировано"]
            for e in active_events:
                print(f"{e.EventID}. {e.Title} ({e.DateTime})")
            event_id = int(input("Введите ID мероприятия: "))
            event = get_event_by_id(event_id)
            if not event or event.Status == "Архивировано":
                print("Мероприятие не найдено или архивировано. ⛔")
                continue

            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            app = Application(
                ParticipantID=participant_id,
                EventID=event_id,
                StaffID=staff_id,
                DateTime=date_time
            )
            app.register()
            print("Заявка зарегистрирована! 📝")

        elif choice == "3":
            app_id = int(input("Введите ID заявки: "))
            app = get_application_by_id(app_id)
            if app:
                print(f"Заявка найдена: Участник {app.ParticipantID} | "
                      f"Мероприятие {app.EventID} | Сотрудник {app.StaffID} | "
                      f"Дата {app.DateTime}")
            else:
                print("Заявка не найдена. ⛔")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")