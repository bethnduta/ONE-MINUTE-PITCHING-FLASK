import unittest
from market.models import Pitch

class Pitch(unittest.TestCase):
    '''
    est Class o est the behaviour of the User
    '''
    def setUp(self):
        '''
        set up method to run before the test
        '''
        self.new_pitch = Pitch("Elevator", "Rachel","test_title","test_author")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))