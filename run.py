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

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()  
def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()
def find_account(username):
    '''
    Function that finds a contact by username and returns the account
    '''
    return User.find_by_username(username) 

def check_existing_accounts(username):
    '''
    Function that check if an account exists with that username and return a Boolean
    '''
    return User.account_exist(username)   
def show_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return User.show_accounts() 
