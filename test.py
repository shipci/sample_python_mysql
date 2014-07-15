import unittest
from sql import Mysql


class test_db(unittest.TestCase):

    def testRowCount(self):
        mql = Mysql()
        mql.populate()
        count = 0
        while True:
            count += 1
            self.failIf(mql.rowcount() != 5)
            res = mql.call_test_proc()
            self.failIf(res[0][0] != 'test proc')
            print "Executed test {0} times".format(count)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
