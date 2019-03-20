import psycopg2

class DataBaseOperations():
    def __init__(self, DATABASE_URL):
        try:
            self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS modeltest"
                                "(username varchar PRIMARY KEY, name varchar,  photo varchar)")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def add_user(self, data):
        tdata = tuple(data.values())
        try:
            print(self.cursor.fetchone())
            self.cursor.execute("INSERT INTO modeltest(username, name, photo) VALUES(%s, %s, %s)", tdata)
            self.conn.commit()
            print(self.cursor.fetchone())
        except (Exception, psycopg2.Error) as error:
            print("Postgres Error in add_user()")
    def check_user(self, username):
        try:
            raw = self.cursor.fetchall()
            if username in raw['username']:
                return username
        except (Exception, psycopg2.Error) as error:
            print("Postgres Error raw = self.cursor.fetchall()")
            print(error)