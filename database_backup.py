import shutil
import datetime


def backup_database():

    source = "hospital.db"

    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_file = f"hospital_backup_{date}.db"

    shutil.copy(source, backup_file)

    print("\nDatabase backup completed successfully!")
    print(f"Backup saved as: {backup_file}")