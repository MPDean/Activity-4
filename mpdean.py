# Michael Dean
# CSCI157
# 2-20-17
import unittest

class User:
    def __init__(self, username, email, ss, password):
        self.username = username
        self.email = Email(email)
        self.ss_num = SS(ss)
        self.hash = Hash(password)
        self.password = password

    def check_password(self, password):
        #Send password to Hash to check it
        print(password)

    def __str__(self):
        return "The username you have created is " + self.username + \
               ". The e-mail address you have selected to use is " + self.email + \
               ".The social security number registered to this account is " + self.ss_num + ". Your password is " + \
               self.password + " and the hash associated with that password is " + self.hash + "."



class FixtureTest(unittest.TestCase):
    def setUp(self):
        print('In setUp()')
        self.fixture = User('MPDean', 'mpd3@alfred.edu', '123-34-4567', '!#CsCi157?')

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('In test()')
        #Email Testing
        #Run test to raise InvalidEmail
        #Social Security Testing
        #Run test to raise InvalidSocial
        #Hash Testing
        #Run test to raise InvalidPassword
        #Run test to see that two same pass generate the same hash



if __name__ == '__main__':
    unittest.main()
    
