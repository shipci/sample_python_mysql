import unittest
from sql import Mysql


class test_db(unittest.TestCase):

    def testRowCount(self):
        mql = Mysql()
        mql.populate()
        #self.failIf(mql.rowcount() != 5)
        res = mql.call_test_proc()
        print res
        self.failIf(res[0] != 'test proc')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
