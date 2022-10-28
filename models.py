import pymysql
import config

db = cursor = None


class MBukuTelepon:
    def __init__(self, no=None, nama=None, no_telp=None):
        self.no = no
        self.nama = nama
        self.no_telp = no_telp

    def openDB(self):
        global db, cursor
        db = pymysql.connect(host=config.DB_HOST, user=config.DB_USER,
                             password=config.DB_PASSWORD, database=config.DB_NAME)
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()

    def selectDB(self):
        self.openDB()
        cursor.execute('SELECT * FROM bukutelepon')
        container = []
        for no, nama, no_telp in cursor.fetchall():
            container.append((no, nama, no_telp))
        self.closeDB()
        return container
