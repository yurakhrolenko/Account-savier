import sqlite3


class Database:

    def __init__(self):
        self.db_name = 'data.db'
        self.table = 'accounts'
        sql = f"CREATE TABLE IF NOT EXISTS {self.table} \
        (id INTEGER PRIMARY KEY, login TEXT, password TEXT, site TEXT, comment TEXT)"
        self.connect()
        self.cur.execute(sql)
        self.conn.commit()
        self.key = 'ghbdtn'

    def connect(self):
        """
        Creates a connection with database
        :return: None
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def insert(self, data_tuple):
        """
        Create a new row in self.table in database
        :param conn:
        :param task:
        :return: lastrowid
        """
        sql = f''' INSERT INTO {self.table} (id,login,password,site,comment) VALUES(NULL,?,?,?,?) '''
        self.connect()
        self.cur.execute(sql, data_tuple)
        self.conn.commit()
        return self.cur.lastrowid

    def view_all(self):
        """
        Retuns all rows from self.table in database
        :return: list if tuples
        """
        sql = f"""SELECT * FROM {self.table}"""
        self.connect()
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        result = []
        for i in rows:
            result.append(i)
        return result

    def update(self, id, login, password, site, comment):
        """
        Updates a row in self.table in database with id = id
        :return: None
        """
        sql = f''' UPDATE {self.table}
                SET login = ? ,
                    password = ? ,
                    site = ? ,
                    comment = ?
                WHERE id = ?'''
        self.connect()
        self.cur.execute(sql, (login, password, site, comment, id))
        self.conn.commit()

    def delete(self, id):
        """
        Deletes a row in self.table in database with id = id
        :return: None
        """
        sql = f"DELETE FROM {self.table} WHERE id=?"
        self.connect()
        self.cur.execute(sql, (id,))
        self.conn.commit()

    def search(self, login='', password='', site='', comment=''):
        """
        Searches all rows in self.table in database where at least one condition mathes.
        :return: list of tuples
        """
        sql = f"""SELECT * FROM {self.table} WHERE login=? OR password=? OR site=? OR comment=?"""
        self.connect()
        self.cur.execute(sql, (login, password, site, comment))
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    db = Database()
