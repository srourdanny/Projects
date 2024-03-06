from functions.functions import *
from classes.database_access import *

my_db = DB_Connect('root', '', 'python_final_database')

programShouldRun = True
while programShouldRun:

    """Show menu options"""
    print("\n1. Import a new data file")
    print("2. Show data currently in a database table")
    print("3. Add a record to the database tables")
    print("4. Edit a record")
    print("5. Delete a record")
    print("6. Exit program")

    """Get user choice"""
    operation = input("Enter a number (1-6) for the operation you'd like to do: ")
    print(operation)

    if operation == "1":
        importingData(my_db)
    elif operation == "2":
        showData(my_db)
    elif operation == "3":
        addData(my_db)
    elif operation == "4":
        editData(my_db)
    elif operation == "5":
        deleteData(my_db)
    elif operation == "6":
        print("Program Exited.")
        programShouldRun = False
        my_db.conn.close()
    else:
        print("Invalid option. Try again.")