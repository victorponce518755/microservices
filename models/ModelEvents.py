from entities.event import event
from flaskl_mysql import MySQLdb

class ModelEvent:
    def __init__(self,mysql):
        self.mysql = mysql


    def get_events(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute('SELECT * FROM evento')
        data = cursor.fetchall()
        cursor.close()
        return data