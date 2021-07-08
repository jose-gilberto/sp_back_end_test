from app import create_app
import json
import unittest

app = create_app()

class GithubApiTest(unittest.TestCase):

    # Setup the basic test_client for test
    def setUp(self) -> None:
        test_app = app.test_client()
        self._app = test_app        


    def test_user_lists(self):
        res = self._app.get('/api/users/')
        res_data = res.json

        self.assertEqual(200, res.status_code)
        # Have data attr and is a list
        self.assertIs(type(res_data['data']), list) 
        # Have attr message and is str
        self.assertIs(type(res_data['message']), str)
        # Have attr status and is int
        self.assertIs(type(res_data['status']), int)
        # Have attr next_page and is str
        self.assertIs(type(res_data['next_page']), str)


    def test_user_details(self):
        res = self._app.get('/api/users/joao/details/')
        res_data = res.json
        
        self.assertEqual(200, res.status_code)
        # Have data attr and is a list
        self.assertIs(type(res_data['data']), dict) 
        # Have attr message and is str
        self.assertIs(type(res_data['message']), str)
        # Have attr status and is int
        self.assertIs(type(res_data['status']), int)


    def test_user_repos(self):
        res = self._app.get('/api/users/joao/repos/')
        res_data = res.json
        
        self.assertEqual(200, res.status_code)
        # Have data attr and is a list
        self.assertIs(type(res_data['data']), list) 
        # Have attr message and is str
        self.assertIs(type(res_data['message']), str)
        # Have attr status and is int
        self.assertIs(type(res_data['status']), int)

