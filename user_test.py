import unittest
from user import User

class TestUserDetails(unittest.TestCase):
    '''
    Test case tests if the user name password match
    '''
    newUserDetails = [] # add empty array to hold new user details

    def setUp(self):
        '''
        set up method run before each test case
        '''
        self.userCredentials = User("Pascal","abc123") # User object

    def test__init__(self):
        '''
        Test if the object is initialized properly
        '''  
def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)

def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the user list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(credentials.credentials_list),1)




if   __name__=='__main__':
    unittest.main()
