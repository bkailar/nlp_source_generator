import unittest
import excel as e


class MyTestCase(unittest.TestCase):

    def test_something(self):
        file_path = '../resources/template.xls'
        excel = e.Excel(file_path)


if __name__ == '__main__':
    unittest.main()
