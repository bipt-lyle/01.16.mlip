import unittest
from app import app

class TestIntegration(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_and_delete_item(self):

        add_response = self.app.post('/add', data={'item': 'Test Item'}, follow_redirects=True)
        self.assertEqual(add_response.status_code, 200) 


        update_response = self.app.post('/update/0', data={'new_item': 'Updated Test Item'}, follow_redirects=True)
        self.assertEqual(update_response.status_code, 200)


        index_response = self.app.get('/')
        self.assertIn(b'Test Item', index_response.data) 

        delete_response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(delete_response.status_code, 200)

 
        updated_index_response = self.app.get('/')
        self.assertNotIn(b'Test Item', updated_index_response.data) 

if __name__ == '__main__':
    unittest.main()
