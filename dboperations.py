import psycopg2

class DataBaseOperations():
    def __init__(self, DATABASE_URL):
        try:
            self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            self.cursor = self.conn.cursor()
            self.conn.autocommit = True
            #self.cursor.execute("CREATE TABLE IF NOT EXISTS users"
            #                    "(username varchar PRIMARY KEY, name varchar,  photo varchar)")
            #self.cursor.execute("CREATE TABLE IF NOT EXISTS model (username varchar PRIMARY KEY,"
            #                    "name varchar, sex varchar, photo varchar, description varchar)")
            self.cursor.execute("CREATE TABLE IF NOT EXISTS records (id serial PRIMARY KEY,"
                                "topic varchar, message varchar)")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
    # Add user to db
    def add_user(self, data):
        # data -> username, name, photo
        if not (self.check_user(data.get('username'))):
            tdata = tuple(data.values())
            try:
                print(tdata)
                #self.cursor.execute("INSERT INTO modeltest(username, name, photo) VALUES(%s, %s, %s)", tdata)
                self.cursor.execute("INSERT INTO users(username, name, sex, photo, description) "
                                    "VALUES(%s, %s, %s, %s, %s)", tdata)
                self.conn.commit()
            except (Exception, psycopg2.Error) as error:
                print("Postgres Error in add_user()", error)
    # Сheck username in db
    def check_user(self, username):
        try:
            self.cursor.execute("SELECT * FROM users")
            raw = self.cursor.fetchall()
            for user in raw:
                if (user[0] == username):
                    return username
        except (Exception, psycopg2.Error) as error:
            print("Postgres Error raw = self.cursor.fetchall()")
            print(error)

    def get_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            raw = self.cursor.fetchall()
            return raw
        except (Exception, psycopg2.Error) as error:
            print("Postgres Error raw = self.cursor.fetchall()")
            print(error)

    def add_record(self, topic, last_chat_text):
        try:
            self.cursor.execute("INSERT INTO records(topic, message) "
                            "VALUES(%s, %s)", (topic, last_chat_text))
            self.conn.commit()
        except (Exception, psycopg2.Error) as error:
            print("Postgres Error in add_record()", error)

    def get_records(self, topic):
        try:
            self.cursor.execute("SELECT * FROM records")
            raw = self.cursor.fetchall()
            print(raw)
            records = []
            for record in raw:
                if (record[1] == topic):
                    records.append(record[2])
            return records
        except (Exception, psycopg2.Error) as error:
            print("Postgres Error raw = self.cursor.fetchall()")
            return None
