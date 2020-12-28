from app import forecast
import unittest


class Test_forecast_Home(unittest.TestCase):
    def setUp(self):
        app = forecast.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)


class Test_forecast_all(unittest.TestCase):
    def setUp(self):
        app = forecast.test_client()
        self.response = app.get('/forecast/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual('application/json', self.response.content_type)


class Test_forecast_code_date(unittest.TestCase):
    def setUp(self):
        app = forecast.test_client()
        self.response = app.get('/forecast/code=huck&date=08-08-2020')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual('application/json', self.response.content_type)


class Test_forecast_date_rage(unittest.TestCase):
    def setUp(self):
        app = forecast.test_client()
        self.response = app.get('/forecast/start_date=25-04-2020&end_date=25-08-2020')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content(self):
        self.assertEqual('application/json', self.response.content_type)


if __name__ == '__main__':
    unittest.main()