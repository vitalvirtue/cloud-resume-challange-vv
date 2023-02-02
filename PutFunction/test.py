
import unittest
import app


class TestAPI(unittest.TestCase):
    def test_getApi_works(self):

        result = app.lambda_handler(0, 0)
        self.assertEqual(result['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()