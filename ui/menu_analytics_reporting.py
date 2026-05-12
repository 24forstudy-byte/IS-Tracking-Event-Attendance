from models.event import get_all_events, get_event_by_id
from models.application import get_all_applications
from models.participant import get_participant_by_id

def menu_reports():
    """Меню аналитики и отчётности"""
    while True:
        print("\n=== Аналитика и отчётность 📊 ===")
        print("1. Список участников по мероприятию")
        print("2. Отчёт по мероприятиям и участникам")
        print("3. Статистика по мероприятиям и участникам")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            print("\n=== Список участников по мероприятию ===")
            event_id = int(input("Введите ID мероприятия: "))
            event = get_event_by_id(event_id)
            if not event:
                print("Мероприятие не найдено. ⛔")
                continue
            all_apps = get_all_applications()
            filtered_apps = [a for a in all_apps if a.EventID == event_id]

            if not filtered_apps:
                print("На это мероприятие ещё никто не зарегистрирован.")
            else:
                print(f"\nСписок участников мероприятия «{event.Title}» (ID: {event_id}):")
                for a in filtered_apps:
                    p = get_participant_by_id(a.ParticipantID)
                    if p:
                        print(f"\n{p.FullName}\nТел: {p.Phone}\nПочта: {p.Mail}")
                    else:
                        print("Участник не найден в базе")

        elif choice == "2":
            print("\n=== Отчёт по мероприятиям и участникам ===")
            events = get_all_events()
            all_apps = get_all_applications()
            if not events:
                print("Нет ни одного мероприятия.")
            else:
                for e in events:
                    count = len([a for a in all_apps if a.EventID == e.EventID])
                    print(f"\n{e.Title}\nДата: {e.DateTime}\nСтатус: {e.Status}\nЗаявок: {count}")

        elif choice == "3":
            print("\n=== Статистика по мероприятиям и участникам ===")
            events = get_all_events()
            all_participants_count = 0  
            all_apps = get_all_applications()
            total_events = len(events)
            total_apps = len(all_apps)

            print(f"Общее количество мероприятий: {total_events}")
            print(f"Общее количество заявок: {total_apps}")
            if total_events > 0:
                average_apps = total_apps / total_events
                print(f"Среднее количество заявок на мероприятие: {average_apps:.1f}")
            else:
                print("Среднее количество заявок на мероприятие: 0")

        elif choice == "0":
            break
        else:
            print("Неверный ввод. 🛑")