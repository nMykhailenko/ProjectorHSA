import csv
import traceback
import pymysql


def seed():
    csv.register_dialect('export_dialect', delimiter=',', quoting=csv.QUOTE_NONE)
    with open('users.csv') as usersFile:
        _ = next(usersFile)

        query = f"INSERT INTO users (first_name, last_name, birthdate) VALUES "
        users = csv.reader(usersFile, 'export_dialect')
        for user in users:
            query += f"({user[1]}, {user[2]}, {user[3]}), "

        query = query[:-2]

        db = pymysql.connect(
            host='localhost',
            user='root',
            password='masterkey',
            database='projector',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()

        print('Connected to db')

        for i in range(4000):
            print(f'#{i} started')
            try:
                cursor.execute(query)
                db.commit()
                print(f"Ended #{i}")
            except Exception as e:
                print(f'error #{i}: {repr(e)}')
                traceback.print_exc()
                db.rollback()
        
        db.close()


seed()
