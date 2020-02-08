#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass


@pytest.fixture(scope="module")
def token(Token, accounts):
    return accounts[0].deploy(Token, "Test Token", "TST", 18, 1e21)


@pytest.fixture(scope="module")
def staking(Staking, accounts):
    token_address = '0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87' # grab from above
    return accounts[0].deploy(Staking, token_address)
