import unittest, time
from sql import Mysql


class test_db(unittest.TestCase):

    def testRowCount(self):
        mql = Mysql()
        mql.populate()
        count = 0
    #while True:
        count += 1
        self.failIf(mql.rowcount() != 5)
        res = mql.call_test_proc()
        self.failIf(res[0][0] != 'test proc')
        print "Executed test {0} times".format(count)
        time.sleep(5)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
