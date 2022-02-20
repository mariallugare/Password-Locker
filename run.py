#!/usr/bin/env python3.9
import unittest
from user import User
import random
import string

def create_contact(username,password):
    '''
    Function to create a new account
    '''
    new_account = User(username,password)
    return new_account
