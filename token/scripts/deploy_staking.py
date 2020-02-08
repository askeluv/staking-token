#!/usr/bin/python3

import os
from brownie import *

def main():
    pk = os.environ.get('ACCOUNT_PRIVATE_KEY')
    accounts.add(pk)
    account = accounts[0]
    print('Account balance', account.balance())
    token_address = '0xb4e8acf5e783d5cb1b943ebb1dcf6f2373b188f9' # D5 Credits (main net)
    Staking.deploy(token_address, {'from': accounts[0]})
