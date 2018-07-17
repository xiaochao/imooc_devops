#coding=utf-8

import unittest
from jenkins import app

class TestJenkins(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(res.data.decode('utf-8'), 'hello world')

if __name__ == '__main__':
    unittest.main()
