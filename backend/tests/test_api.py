import unittest
from flask import url_for
from app import create_app


class APIHostsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        if self.app_context:
            self.app_context.pop()

    def test_alive(self):
        response = self.client.get(url_for("main.get_hosts_api"))
        self.assertEqual(response.status_code, 200)


class APIFuncResultsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        if self.app_context:
            self.app_context.pop()

    def test_alive(self):
        response = self.client.get(
            url_for("main.get_results_api", name="test", func="test")
        )
        self.assertEqual(response.status_code, 200)
