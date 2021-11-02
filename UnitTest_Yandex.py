import unittest
from yandex_API import create_folder
import yandex_API



class TestYandexApi(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(create_folder(yandex_API.headers,'Yandex_API'), 201)