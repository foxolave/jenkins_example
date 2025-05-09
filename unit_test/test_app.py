import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'running_v1'})

if __name__ == '__main__':
    unittest.main()
