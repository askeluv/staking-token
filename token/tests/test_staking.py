#!/usr/bin/python3

def test_staking(token, staking, accounts):
    stake_amount = 1e20
    unstake_amount = 1e20
    balance_before_staking = token.balanceOf(accounts[0])
    expected_balance_after_staking = balance_before_staking - stake_amount
    token.approve(staking.address, stake_amount, {'from': accounts[0]})
    assert token.allowance(accounts[0], staking.address) == stake_amount
    staking.stake(stake_amount, {'from': accounts[0]})
    assert staking.stakedAmount(accounts[0]) == stake_amount
    assert token.balanceOf(accounts[0]) == expected_balance_after_staking
    staking.unstake(stake_amount, {'from': accounts[0]})
    assert staking.stakedAmount(accounts[0]) == 0
    assert token.balanceOf(accounts[0]) == balance_before_staking
