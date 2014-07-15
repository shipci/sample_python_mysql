import MySQLdb as mdb
import sys


class Mysql():
    def populate(self):
        con = None
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS messages;")
            cur.execute("CREATE TABLE messages(message varchar(200));")
            cur.execute("insert into messages(message) VALUES('this is test message 1');")
            cur.execute("INSERT INTO messages(message) VALUES('this is test message 2');")
            cur.execute("INSERT INTO messages(message) VALUES('this is test message 3');")
            cur.execute("INSERT INTO messages(message) VALUES('this is test message 4');")
            cur.execute("INSERT INTO messages(message) VALUES('this is test message 5');")
            con.commit()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            con.close()

    def call_test_proc(self):
        con = None
        try:
            con = self.connect()
            cur = con.cursor()
            cur.callproc('test_proc')
            result = cur.fetchall()
            return result
        finally:
            con.close()

    def rowcount(self):
        con = None
        try:
            con = self.connect()
            cur = con.cursor()
            cur.execute("select * from messages;")
            cnt = cur.fetchall()
            return len(cnt)
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

        finally:
            con.close()

    def connect(self):
        con = mdb.connect('127.0.0.1', 'shippable', '', 'test')
        return con

    def disconnect(self):
        if self.con:
            self.con.close()


if __name__ == '__main__':
    mysql = Mysql()
    mysql.populate()
    mysql.rowcount()
