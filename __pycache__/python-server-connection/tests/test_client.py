import unittest
from src.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_connect(self):
        result = self.client.connect()
        self.assertTrue(result)

    def test_send_data(self):
        self.client.connect()
        response = self.client.send_data("Hello, Server!")
        self.assertEqual(response, "Data sent successfully")

    def test_receive_data(self):
        self.client.connect()
        self.client.send_data("Hello, Server!")
        response = self.client.receive_data()
        self.assertIsNotNone(response)

    def tearDown(self):
        self.client.disconnect()

if __name__ == '__main__':
    unittest.main()