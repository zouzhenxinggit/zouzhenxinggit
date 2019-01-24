"""

This module encapsulates the operation of the database, very convenient

"""
import MySQLdb


class MysqlHelper(object):
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def __str__(self):
        return "this MysqlHelper"

    def connect(self):
        self.conn = MySQLdb.connect(host = self.host,
                                    port = self.port,
                                    db = self.db,
                                    user = self.user,
                                    passwd = self.passwd,
                                    charset = self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    '''insert data'''
    def insert(self, sql, params=[]):
        return self.__cud(sql, params)

    '''update data'''
    def update(self, sql, params=[]):
        return self.__cud(sql, params)

    '''delete data'''
    def delete(self, sql, params=[]):
        return self.__cud(sql, params)

    def __cud(self, sql, params=[]):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception ,e:
            print e.message
        return count

    '''Query a row of data'''
    def fetchone(self, sql, params=[]):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception, e:
            print e.message
        return result

    '''Query multiple rows of data'''
    def fetchall(self, sql, params=[]):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
        except Exception, e:
            print e.message
        return result