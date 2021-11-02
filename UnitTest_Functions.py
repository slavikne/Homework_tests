import unittest
from test_functions import output_name, out_directories, output_list_document, add_document, del_document, \
    move_document, add_shelf
import test_functions



class TestFunctions(unittest.TestCase):

    def test_output_name(self):
        self.assertEqual(output_name("10006"), 'Аристарх Павлов')

    def test_out_directories(self):
        self.assertEqual(out_directories('2207 876234'), '1')

    def test_output_list_document(self):
        self.assertEqual((output_list_document()),test_functions.documents)

    def test_add_document(self):
        self.assertIn(add_document('passport', '123456', 'Иван Дулин', '2'), test_functions.documents)

    def test_del_document(self):
        self.assertIsNot(del_document('11-2'), test_functions.documents)

    def test_move_document(self):
        self.assertIn(move_document('20006', '3'), test_functions.directories['3'])
        self.assertNotIn(move_document('20006', '3'), test_functions.directories['2'])

    def test_add_shelf(self):
        self.assertIn(add_shelf('4'), test_functions.directories)


if __name__ == '__main__':
    unittest.main()
