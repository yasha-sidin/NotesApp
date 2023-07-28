from ViewController.ViewController import ViewController

class main():

    if __name__ == '__main__':
        database_name = "new_notes_big_data"
        table_name = "your_notes"
        logger_path = "./logs/logs"
        icon_path = "sourses/note_102351.ico"
        title = "Your notes"
        app = ViewController(database_name, table_name, logger_path, icon_path, title)
        app.initialize()

