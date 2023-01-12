import unittest
import requests as r


class Test(unittest.TestCase):
    def test_reefbook_without_date(self):
        resp = r.get("http://127.0.0.1:8000/api/v1/reefbooks").json()

        valid_response = {
            "refbooks": [
                {"id": 3, "code": "codsse", "name": "name"},
                {"id": 4, "code": "sdvasdv", "name": "avsdv"},
            ]
        }
        self.assertEqual(resp, valid_response)

    def test_reefbook_with_date(self):
        date = "2023-01-11"
        resp = r.get(f"http://127.0.0.1:8000/api/v1/reefbooks?date={date}").json()

        valid_response = {"refbooks": [{"id": 3, "code": "codsse", "name": "name"}]}
        self.assertEqual(resp, valid_response)

    def test_reefbook_with_date(self):
        date = "2023-01-11"
        resp = r.get(f"http://127.0.0.1:8000/api/v1/reefbooks?date={date}").json()
        valid_response = {"refbooks": [{"id": 3, "code": "codsse", "name": "name"}]}
        self.assertEqual(resp, valid_response)

    def test_element(self):
        id = 3
        version = 0
        resp = r.get(
            f"http://127.0.0.1:8000/api/v1/reefbooks/{id}/check_element?version={version}"
        ).json()

        valid_response = {"status":True}
        self.assertEqual(resp, valid_response)

    def test_check_element(self):
        code = "ae"
        value = "ewqrwer"
        id = 3
        version = 0
        resp = r.get(
            f"http://127.0.0.1:8000/api/v1/reefbooks/{id}/elements?version={version}"
            f"&code={code}&value={value}"
        ).json()

        valid_response = {"elements": [{"code": "ae", "value": "ewqrwer"}]}
        self.assertEqual(resp, valid_response)


if __name__ == "__main__":
    unittest.main(failfast=True, exit=False)
