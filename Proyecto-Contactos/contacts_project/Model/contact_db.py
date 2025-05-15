import sqlite3 as db

class ContactDB:

   def creating_DB():
    try:
     Db = db.connect("Contacts.db")
     print("Succesfull!!")

    except Exception as e:
     print("Fatal error we cannot creat a DB",e)

    finally : Db.close()

   def creating_tables():
      try:
         Db = db.connect("Contacts.db")
         cur = db.Cursor(Db)
         TableQuery = "CREATE TABLE contacts (id INT, contact_name TEXT, contact_number INT)"
         cur.execute(TableQuery)
      except Exception as e:
        print("Unable to create",e)

      finally:
       Db.close()

