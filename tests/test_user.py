import unittest
from market.models import User

class User(unittest.TestCase):
    '''
    est Class o est the behaviour of the User
    '''
    def setUp(self):
        '''
        set up method to run before the test
        '''
        self.new_user = User("beth", "business","test_title","test_author")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))    