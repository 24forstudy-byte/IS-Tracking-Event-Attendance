from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_event import menu_event
from ui.menu_application_participant import menu_application, menu_participant
from ui.menu_analytics_reporting import menu_reports
from ui.menu_references import menu_references

def main():
    initialize_db()

    while True:
        user_choice = show_main_menu()

        if user_choice == "1":
            menu_event()
        elif user_choice == "2":
            menu_application_participant()
        elif user_choice == "3":
            menu_reports()
        elif user_choice == "4":
            menu_references()
        elif user_choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()