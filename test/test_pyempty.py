# -*- coding:utf-8 -*-

import pyempty
import unittest


class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version(self):
        self.assertIsNotNone(pyempty.__version__, '0.1')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_version'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
